from r_app.awesome_generator.core import extractor


def test_get_github_collection_results():
    test_collection_id = "open-journalism"
    collection_results = extractor.get_github_collection_results(test_collection_id, 20)
    print(collection_results)
