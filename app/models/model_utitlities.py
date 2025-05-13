from datetime import datetime
import pytz

def date_to_str(
    dt: datetime,
    fmt: str = "iso",
    tz: str = "UTC"
) -> str:
    """
    Convert a datetime object to a string.
    
    Args:
        dt (datetime): The datetime object to format.
        fmt (str): "iso" for ISO 8601, or any strftime format.
        tz (str): Time zone string (e.g., "UTC", "US/Pacific").

    Returns:
        str: Formatted datetime string.
    """
    if not dt:
        return ""

    try:
        tz_obj = pytz.timezone(tz)
        dt = dt.astimezone(tz_obj)
    except Exception:
        pass  # fallback to naive datetime if timezone is invalid or missing

    if fmt == "iso":
        return dt.isoformat()
    else:
        return dt.strftime(fmt)
