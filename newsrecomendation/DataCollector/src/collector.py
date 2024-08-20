from newsrecomendation.DataCollector.src.dataAnalyzerProducer import DataAnalyzerProducer
from newsCollectorService import NewsCollectorService


def main():
    try:
        service = NewsCollectorService()
        sources = service.get_sources()
        producer = DataAnalyzerProducer()

        for s in sources:
            print(f'Source {s["id"]}')

            articles = service.get_articles(source=s["id"])
            print(f'Articles count: {len(articles)}')
            for a in articles:
                print(a)
                na = service.save_article(a)
                if na is not None:
                    print(f"{na.id} -> {na.url}")

        producer.send_message()
    except:
        print("An exception occurred")


if __name__ == "__main__":
    main()
