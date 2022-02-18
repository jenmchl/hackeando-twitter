import twint

search = input('O que você está buscando? ')
city = input('Onde? ')

c = twint.Config()
c.Search = search
c.Near = city
c.Limit = 20
c.Populer_tweets = True

twint.run.Search(c)
