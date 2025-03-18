from .formatting import format_author, format_date, format_title, format_website


class APACitationGenerator:
    def __init__(self, author, date, title, website, url):
        self.author = author
        self.date = date
        self.title = title
        self.website = website
        self.url = url

    def is_chinese_document(self):
        chinese_count = 0
        total_count = 0

        for char in self.title:
            # 使用Unicode範圍來判斷字符是否是中文
            if '\u4e00' <= char <= '\u9fff':
                chinese_count += 1
            total_count += 1

        chinese_ratio = chinese_count / total_count

        # 如果中文字符佔比大於70%，則判斷為中文文獻
        if chinese_ratio > 0.7:
            return True
        else:
            return False

    def generate_apa_citation(self):
        is_chinese = self.is_chinese_document
        formatted_author = format_author(self.author, is_chinese)
        formatted_date = format_date(self.date)
        formatted_title = format_title(self.title, is_chinese)
        formatted_website = format_website(self.website, is_chinese)

        citation = f"{formatted_author}（{formatted_date}）。{formatted_title}。{formatted_website}。{self.url}"

        return citation
