from datetime import datetime


def format_author(author, lang):
    if lang:
        # 中文文獻的作者格式
        authors = author.split("、")
        num_authors = len(authors)
        if num_authors <= 20:
            formatted_author = "、".join(authors)
        else:
            formatted_author = "、".join(authors[:19]) + "···"
    else:
        # 英文文獻的作者格式
        authors = author.split(",")
        num_authors = len(authors)
        if num_authors <= 20:
            if num_authors <= 2:
                formatted_author = " & ".join(authors)
            else:
                formatted_author = ", ".join(authors[:-1]) + ", & " + authors[-1]
        else:
            formatted_author = ", ".join(authors[:19]) + ", ..."

    return formatted_author


def format_date(date, lang):
    # 定義支援的日期格式列表
    supported_formats = ["%Y-%m-%d", "%Y/%m/%d", "%Y%m%d"]

    formatted_date = None

    if lang:
        for fmt in supported_formats:
            try:
                parsed_date = datetime.strptime(date, fmt)
                formatted_date = parsed_date.strftime("%Y年%m月%d日")
                break
            except ValueError:
                continue

        return formatted_date
    else:
        for fmt in supported_formats:
            try:
                parsed_date = datetime.strptime(date, fmt)
                formatted_date = parsed_date.strftime("%Y, %B %d")
                break
            except ValueError:
                continue

        return formatted_date


def format_title(title, lang):
    if lang:
        # 中文文獻的標題格式
        formatted_title = f"**{title}**"
    else:
        # 英文文獻的標題格式
        formatted_title = f"*{title}*"

    return formatted_title


def format_website(website, lang):
    # 在這裡實現你的網站名稱格式化邏輯
    # 例如，將網站名稱轉換為大寫
    formatted_website = website.upper()
    return formatted_website
