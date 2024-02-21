-- Create the Recipe Database
CREATE DATABASE RecipeDatabase;

-- Switch to the Recipe Database
USE RecipeDatabase;

-- Create the Recipes table
CREATE TABLE Recipes (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
);

-- Insert some sample data
INSERT INTO Recipes (name, ingredients, instructions) 
VALUES 
    ('Canjeero','Flour, Sugar, Water, Milk', 'Heat pan on medium high heat. Mix all ingredients together in a big bowl. Using a ladle scoop some of the batter and slowly pour into pan. Quickly use the bottom of the ladle to create a circular motion spreading the batter. Cook until both sides golden brown.'),
    ('Attieke Garba','Cassava couscous+Fish+Onion+Tomato+ Pepper+bouillon+oil' , 'Cook the cassava couscous according to packaging instructions. Fry fish. Add tomato, onion pepper, bouillon and oil.'),
    ('Waakye','Rice+Beans+salt+baking sodaspicy sauce','Cook rice and beans together in the same pan. Add baking soda and salt. Once ready add your shito sauce.'),
    ('Vegetarian Stir-Fry', 'Tofu, broccoli, bell peppers, soy sauce, rice', '1. Stir-fry tofu and vegetables, 2. Add soy sauce, 3. Cook rice, 4. Serve.'),
	('Jollof','Rice+Tomato+Tomato Paste+Grilled Mackerel+Onion+oil+Bell peppers+Salt+Spices(Onga and Jollof spices)+Beef+Garlic+Ginger+Bay leaves','Blend ginger with garlic onions pepper and seeds of bell pepper. Blend tomatoes. Steam beef with blended ginger galic and onions. Put a little oil on fire set to medium heat. Add bay leaves and chopped onions. Add blended mixtures and allow to cook for 20 minutes. Add chunks of grilled mackerel and spices.| Let it cook for 10 more minutes and add the stock from your beef.|After 20 mins, add your washed rice with a little water and salt to taste. | Set on medium low heat and stair after 20 mins.| Cover with a foil paper, set to low heat and let it cook for 30 mins.'),
	('Fufu and light soup','Carrots or Garden eggs+ Neat Fufu+Goat meat+Ginger+Garlic+ Tomatoes+Peppers+Tomato Paste+Onga Spice(To taste)', 'Steam Goat meat with tomato, onions and carrots. Blend the steamed ingredients and add to meat and stock and let cook till done. Add you onga cube or any natural soaup spice. Stir your fufu on medium low heat.'),
	('Sambusa','Egg roll wrapper+Ground Beef+Serrano Peppers+Onion+Vegetable Oil+Salt+Pepper+water', 'Fill a medium to large-sized pot with oil about 1/4 of the way and preheat. Using a pan, saute the onions until golden brown. Add serrano peppers and water and saute until water evaporates. Add ground beef and seasonings and saute until browned. Dump onions, serrano pepper, and ground beef into a seperate bowl. Take an egg roll wrapper and fold the sides in to make mini triangles. Fill with meat mixture and seal. Fry on both sides until golden brown and cool.'),
	('Bisbaas Habashi','Jalapeno pepper, garlic, onion, salt+water', 'Finely chop the jalapeno and vegetables. Place into blender with water and salt. Blend.'),
	('Kelewele','Riped Plantain, ginger, garlic, red pepper', 'Slice the plantains lengthwise. Roughly chop the fresh ginger and onions. Let the plantains sit and marinate in blended mixture. Heat cooking oil in a deep pan or pot over medium heat. Fry the plantain cubes until they turn golden brown. Transfer the fried kelewele onto a plate lined with paper towels to absorb any remaining oil.'),
	('Bariis Iskukaris','Basmati rice, Chicken Boullion, Onion, Olive Oil, Cinnamon Stick, Clove, Cardamom pods, Goat, Garlic, Cumin, Add all ingredients except rice to a pot and boil for three hours. When there is 30 minutes remaining add the rice and cover the lid.');


-- Query to retrieve recipes
SELECT * FROM Recipes;
