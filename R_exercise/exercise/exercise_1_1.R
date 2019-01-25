library("dplyr")
library("gapminder")

gapminder

gapminder %>% 
  filter(year == 2007 ) %>%
  group_by(country) %>%
  summarise(mean_gdpc = mean(gdpPercap))

# 2007년 나라별 1인당 국민소득


gapminder %>%
  filter(year == 2007) %>%
  group_by(continent) %>%
  summarise(mean(lifeExp), median(lifeExp))

# 2007년 대륙별 일인당 평균수명의 평균과 중앙값



