# Previous input
seconds = int(input("Enter duration in seconds: "))

# Process
def humanize_Duration(seconds):
    secs = int(seconds)
    if secs == 0:
        return "0 seconds"
    days, rem = divmod(secs, 86400)
    hours, rem = divmod(rem, 3600)
    minutes, s = divmod(rem, 60)
    parts = []
    if days:
        parts.append(f"{days} day{'s' if days > 1 else ''}")
    if hours:
        parts.append(f"{hours} hour{'s' if hours > 1 else ''}")
    if minutes:
        parts.append(f"{minutes} minute{'s' if minutes > 1 else ''}")
    if s:
        parts.append(f"{s} second{'s' if s > 1 else ''}")
    return ", ".join(parts) if parts else "0 seconds"

# Post process
print("Humanized duration:", humanize_Duration(seconds))
