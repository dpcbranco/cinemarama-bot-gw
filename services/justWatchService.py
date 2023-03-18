from justwatch import JustWatch

just_watch = JustWatch(country='BR')

def search(query):
    response = just_watch.search_for_item(query=query)
    movieList = {movie["jw_entity_id"]:"{} ({})".format(movie["title"], movie["original_release_year"]) for movie in response["items"][:10]}
    return movieList