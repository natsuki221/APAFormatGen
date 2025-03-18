from citation.citation_generator import APACitationGenerator


def main():
    # 使用者輸入
    author = input("請輸入作者名稱：")
    date = input("請輸入日期：")
    title = input("請輸入文章標題：")
    website = input("請輸入網站名稱：")
    url = input("請輸入網址：")

    # 產生APA格式的引文
    citation_generator = APACitationGenerator(author, date, title, website, url)
    apa_citation = citation_generator.generate_apa_citation()

    # 輸出APA格式引文
    print("APA格式引文：")
    print(apa_citation)


if __name__ == '__main__':
    main()
