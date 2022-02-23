import requests, json, os

BASE_URL = 'http://127.0.0.1:5000/'
path_base = os.path.dirname(os.path.abspath(__file__))

def get_exam_version():
	return 'a'
	# return 'b'
	# return 'c'


#obtener todos los posts
def get_all_posts():
    r = requests.get(f'{BASE_URL}posts')
    if r.status_code != 200:
        return []
    else:
        return r.json()

#funcion que te devuelve un post dependiendo de la id que introduzcas
def get_posts_by_id(id_post):
    posts = get_all_posts()
    for post in posts:
        if post['id'] == id_post:
            return post

#funciom que te devuelve el comentario dependiendo del id comentario que
def get_comment_by_id(id_comentario):
	r = requests.get(f'{BASE_URL}comments/{id_comentario}')
	comentario = r.json()
	return comentario


def ejercicio1():
	#devolver el numero de posts que tengan comentarios
	posts_con_comentarios = []
	ids_post_comentario = []
	r = requests.get(f'{BASE_URL}comments')
	comentarios = r.json()
	for comentario in comentarios:
		ids_post_comentario.append(comentario['postId'])
	for ids_post in ids_post_comentario:
		posts_con_comentarios.append(get_posts_by_id(ids_post))
	#print(json.dumps(posts_con_comentarios,indent=4))
	numero_posts = len(posts_con_comentarios)
	return numero_posts

def ejercicio2():
	#devolver el email de la persona que escribio "nice job, jennifer" dentro de un comentario
	r = requests.get(f'{BASE_URL}comments')
	comentarios = r.json()
	ids_comentarios=[]
	comentarios_con_body=[]
	email = ""
	texto = "quia molestiae reprehenderit Nice job, Jennifer! quasi aspernatur\naut expedita occaecati aliquam eveniet laudantium\nomnis quibusdam delectus saepe quia accusamus maiores nam est\ncum et ducimus et vero voluptates excepturi deleniti ratione"
	for coment in comentarios:
		ids_comentarios.append(coment['id'])
	for ids in ids_comentarios:
		comentarios_con_body.append(get_comment_by_id(ids))
	#print(comentarios_con_body)
	for comentario in comentarios_con_body:
		if comentario['body'] == texto:
			email = comentario['email']
			print(email)
			return email

def ejercicio3():
	#modificar los posts sumando 100 a cada userId, si un post tuviera id 5 se queda como 105
	posts_encontrados= []
	posts= get_all_posts()
	for post in posts:
		posts_encontrados.append(post)
	print(posts_encontrados)
	#modificacion de los posts
	for post in posts_encontrados:
		post_editado={
			"userId": post['userId'] + 100,
		}
		r = requests.put(f'{BASE_URL}posts/{post["id"]}',json=post_editado)
		if r.status_code != 200:
			print('se ha modificiado correctamente el idusuario del post')
		else:
			print('NO se ha podido modificar el idusuario de post')
	return

def ejercicio4():
	#borrar todos lo posts que tengan el body vacio
	posts = get_all_posts()
	posts_con_body = []
	for post in posts:
		r = requests.get(f'{BASE_URL}posts/{post["id"]}')
		posts_con_body.append(r.json())
	for post in posts_con_body:
		if post['body'] == "":
			r = requests.delete(f'{BASE_URL}posts/{post["id"]}')
			if r.status_code == 200:
				print('Se ha borrado el post correctamente')
			else:
				print('NO se ha podido borrar')
	return

def ejercicio5():
	#crear un nuevo comentario con los datos leidos del archivo new_comment.json, este comentario tiene que estar asociado
	#al post con id mas bajo, la funcion retorna el is asignado al nuevo comment

	#obtenemos el new comentario
	
	with open(f'{path_base}/new_comment.json', 'r', encoding='UTF-8') as file:
		comentario =file.read()
	
	#No he conseguido transformar la string que me deveuele el file.read en un diccionario
	#es lo unico que me falta para poder acceder a los datos del comentario y poder poner un nuevo comentarrio
	comentario = json.loads(comentario)
	posts = get_all_posts()
	ids_posts=[]
	for post in posts:
		ids_posts.append(post['id'])
	minimo_id_post = min(ids_posts)
	print(comentario)
	nuevo_comentario={
		"postId":minimo_id_post,
		"email": comentario['email'],
		"name":comentario['name'],
		"body":comentario['body']
	}

	r = requests.post(f'{BASE_URL}comments',json=nuevo_comentario)
	if r.status_code == 200:
		print('Se ha podido meter un nuevo comentario')
	else:
		print('FALLO')

	r = requests.get(f'{BASE_URL}comments')
	comentarios = r.json()
	for coment in comentarios:
		if coment['postId'] == minimo_id_post:
			return coment['id']

# No tocar
def reset_data(data = 'a'):
	requests.post(f'{BASE_URL}data/{data}')

def main():
	reset_data()
	print(ejercicio1())
	print(ejercicio2())
	print(ejercicio3())
	print(ejercicio4())
	print(ejercicio5())

# No tocar
if __name__ == "__main__":
	main()