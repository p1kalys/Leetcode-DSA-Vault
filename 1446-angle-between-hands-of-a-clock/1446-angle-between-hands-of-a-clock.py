class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        if hour == 12:
            hour = 0
        if minutes == 60:
            minutes = 0
            hour += 1
            if hour > 12:
                hour = hour - 12
        angle_h = (30 * hour) + (minutes * 0.5)
        angle_m = 6 * minutes
        angle = abs(angle_h - angle_m)
        angle = min(360 - angle, angle)
        return angle