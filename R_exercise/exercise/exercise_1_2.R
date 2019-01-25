
google_review_data <- read.csv("google_review_ratings.csv")

datasets_data <- read.csv("datasets.csv")

fifa19_data <- read.csv("fifa19_data.csv")

google_review_data
head(google_review_data , 5)
google_review_data %>% 
  group_by(User) %>%
  summarise(mean(Category.1))

head(datasets_data)

datasets_data %>%
  group_by(Title) %>%
  summarise(any(has_logical))


head(fifa19_data, 5)
fifa19_data %>%
  filter(Club == "FC Barcelona")%>%
  group_by(Nationality) %>%
  summarise(mean(Overall))

