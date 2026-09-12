from client import ProductReviewSentimentAnalyzerClient

def main():
    client = ProductReviewSentimentAnalyzerClient()
    res = client.analyze_reviews()
    print("=== Product Review Sentiment Analyzer Output ===")
    print(f"Product: {res['product_name']} | Verdict: {res['verdict']}")
    print(f"Avg Rating: {res['average_star_rating']}/5.0 | Net Sentiment Index: {res['net_promoter_index']}")
    print(f"Verified Purchases: {res['verified_purchase_percentage']}")
    print("\nAspect Satisfaction Radar (0-10):")
    for aspect, score in res['aspect_breakdown'].items():
        print(f"  • {aspect:<18}: {score}/10.0")

if __name__ == '__main__':
    main()
