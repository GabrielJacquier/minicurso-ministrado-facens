import requests, json

URL_IMAGES = "http://image.tmdb.org/t/p/w185/"

def request_filmes():
    params = {
    	'api_key': '8c348d8df5000d4848560eee211505ca',
    	'sort_by': 'popularity.desc',
    	'language': 'pt'
    }
    response = requests.get("http://api.themoviedb.org/3/discover/movie",
        params=params)
    # import pdb; pdb.set_trace()
    # return response.json()['results']
    return response.text

conteudo = request_filmes()
json_filmes = json.dumps(conteudo, indent=4)