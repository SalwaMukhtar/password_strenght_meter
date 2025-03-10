import re
import string
import random
from typing import Tuple, List

class PasswordStrengthMeter:
    def __init__(self):
        self.common_passwords = {
            'password123', '12345678', 'qwerty123', 'admin123',
            'letmein123', 'welcome123', 'monkey123', 'football123'
        }
        
        self.special_chars = '!@#$%^&*'
        self.feedback = []
        
    def generate_strong_password(self, length: int = 12) -> str:
        """Generate a strong random password."""
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        
        # Ensure at least one of each required character type
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(self.special_chars)
        ]
        
        # Fill the rest with random characters
        all_chars = lowercase + uppercase + digits + self.special_chars
        for _ in range(length - 4):
            password.append(random.choice(all_chars))
            
        # Shuffle the password
        random.shuffle(password)
        return ''.join(password)
    
    def check_password_strength(self, password: str) -> Tuple[int, List[str], str]:
        """Check password strength and return score, feedback, and strength rating."""
        self.feedback = []
        score = 0
        
        # Check if password is in common passwords list
        if password.lower() in self.common_passwords:
            self.feedback.append("❌ This is a commonly used password. Please choose something more unique.")
            return 0, self.feedback, "Very Weak"
        
        # Length Check (weight: 1)
        if len(password) >= 12:
            score += 1
        elif len(password) >= 8:
            score += 0.5
            self.feedback.append("⚠️ Consider using a longer password (12+ characters recommended).")
        else:
            self.feedback.append("❌ Password must be at least 8 characters long.")
        
        # Upper & Lowercase Check (weight: 1)
        if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
            score += 1
        else:
            self.feedback.append("❌ Include both uppercase and lowercase letters.")
        
        # Digit Check (weight: 1)
        if re.search(r"\d", password):
            score += 1
        else:
            self.feedback.append("❌ Add at least one number (0-9).")
        
        # Special Character Check (weight: 1)
        if re.search(f"[{re.escape(self.special_chars)}]", password):
            score += 1
        else:
            self.feedback.append(f"❌ Include at least one special character ({self.special_chars}).")
        
        # Determine strength rating
        if score >= 4:
            strength = "Strong"
            if not self.feedback:
                self.feedback.append("✅ Excellent! Your password meets all security criteria.")
        elif score >= 3:
            strength = "Moderate"
            if not self.feedback:
                self.feedback.append("⚠️ Good password, but could be stronger.")
        elif score >= 2:
            strength = "Weak"
        else:
            strength = "Very Weak"
            
        return score, self.feedback, strength 