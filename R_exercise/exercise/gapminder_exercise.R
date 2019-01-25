library("gapminder")

gapminder[, c('lifeExp', 'gdpPercap')]
gapminder %>% select(gdpPercap, lifeExp)

summary(gapminder$lifeExp)
summary(gapminder$gdpPercap)

?cor

cor(gapminder$lifeExp , gapminder$gdpPercap)

opar = par(mfrow=c(2,2))
hist(gapminder$lifeExp)
hist(gapminder$gdpPercap, nclass=50)
hist(log10(gapminder$gdpPercap), nclass = 50)
plot(log10(gapminder$gdpPercap), gapminder$lifeExp, cex=.5)
par(opar)