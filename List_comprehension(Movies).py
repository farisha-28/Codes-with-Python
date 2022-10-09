movies = [("Yuksek",1950),("Bizim",1900),("Biz Boyeleyiz",2000),("Muzz",2001)]
new_movies = [title for(title,year) in movies if year<2000]
print(new_movies)