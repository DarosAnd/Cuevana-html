# {% if estado == 0 %}
#                     <a href="/LikePelicula?id={{pelicula.idTitulo}}">
#                         <button type="button">Like</button>
#                     </a>
#                 {% else %}
#                     <a href="/DislikePelicula?id={{pelicula.idTitulo}}">
#                         <button type="button">Dislike</button>
#                     </a>
#                 {% endif %}
#
#                 {{likes}}
#             </center>
#
#             <div>
#                 <form method="POST" action="/Comentario">
#                     <input type="hidden" name="idPelicula" value="{{pelicula.idTitulo}}">
#                     <input type="text" size="100" name="inputComment" id="inputComment" placeholder="Agregar Comentario" required>
#                     <button type="submit" class="float">submit</button>
#                 </form>
#             </div>
#
#             <h1>Comentarios</h1>
#
#             {% for item in comentarios %}
#                 <h6>@{{item.Usuario.nickName}} || {{item.descripcion}} </h6>
#             {% endfor %}