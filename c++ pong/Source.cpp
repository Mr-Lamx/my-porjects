#include<SFML/Graphics.hpp>
#include<iostream>
#include<string>


int main()
{
	double width = 800;
	double height = 800;
	
	//creating the window
	sf::RenderWindow window(sf::VideoMode(width, height), "test", sf::Style::Close | sf::Style::Resize);
	sf::Font font;
	sf::Text score1;
	sf::Text score2;

	font.loadFromFile("04B_30__.TTF");

	score1.setFont(font);
	score2.setFont(font);


	// creating all the shapes
	sf::CircleShape player(10.0f);
	sf::RectangleShape player1(sf::Vector2f(20.0f, 100.0f));
	sf::RectangleShape player2(sf::Vector2f(20.0f, 100.0f));
    


	player.setOrigin(15.0f, 15.0f);

	


	sf::Event evnt;
	//giving the shapes their starting postions
	player.setPosition(400, 400);
	player1.setPosition(200, 0);
	player2.setPosition(600, 0);
	score2.setPosition(750, 0);
	

	double xvel = 0;
	double yvel = 0;

	
	int scor1 = 0;
	int scor2 = 0;
	
	//creating the main game loop
	while (window.isOpen())
	{
		//getting all the event
		while (window.pollEvent(evnt))
		{
			if (evnt.type == evnt.Closed)
			{
				window.close();
			}
		}
		window.clear();
		score1.setString(std::to_string(scor1));
		score2.setString(std::to_string(scor2));
		
		//drawing the shapes to the window

		window.draw(player1);
		window.draw(player);
		window.draw(player2);
		window.draw(score1);
		window.draw(score2);

		window.display();


        //moving the ball according to it's velocity

		player.move(xvel, yvel);
		double movmentspeed = 0.0001;
		

		//getting the position of the ball
		float x = player.getPosition().x;
		float y = player.getPosition().y;

		
		double randNum = rand() % (0 - (-1) + 1) + -1;
		double randNum1 = rand() % (0 - (-1) + 1) + -1;

		//checking if the ball collides with the players and making it bounce
		//checking if it collided with player1

		int a = 1;
		if (player.getGlobalBounds().intersects(player1.getGlobalBounds()))
		{
			
			if (a == 1) {
				yvel = yvel * randNum;
				xvel = xvel * -1;
				a = a * -1;
			}
			else {
				yvel = yvel * randNum1;
				xvel = xvel * -1;
				a = a * -1;
			}
			
			

		}
		if (player.getGlobalBounds().intersects(player2.getGlobalBounds()))
		{
			

			if (a == 1) {
				yvel = yvel * randNum;
				xvel = xvel * -1;
				a = a * -1;
			}
			else {
				yvel = yvel * randNum1;
				xvel = xvel * -1;
				a = a * -1;
			}

		}



		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Space))
		{
			xvel = xvel - 0.0002;
			yvel = yvel - 0.0002;
		}

		//moving player 1
		if (sf::Keyboard::isKeyPressed(sf::Keyboard::W))
		{
			player1.move(0, -0.1);
		}

		if (sf::Keyboard::isKeyPressed(sf::Keyboard::S))
		{
			player1.move(0, 0.1);
		}


		//moving player2
		if (sf::Keyboard::isKeyPressed(sf::Keyboard::I))
		{
			player2.move(0, -0.1);
		}

		if (sf::Keyboard::isKeyPressed(sf::Keyboard::K))
		{
			player2.move(0, 0.1);
		}
		 
		

		 


		//checking if the ball gets out of the window 
		if (x >= 770.0f)
		{
			player.setPosition(400, 400);
			scor1 = scor1 + 1;
			yvel = 0;
			xvel = 0;
		}
		if (x <= 0.0f)
		{
			player.setPosition(400, 400);
			scor2 = scor2 + 1;
			yvel = 0;
			xvel = 0;
		}
		if (y >= 770.0f)
		{
			xvel = xvel * -1;
			yvel = yvel * -1;
		}
		if (y <= 0.0f)
		{
			xvel = xvel * -1;
			yvel = yvel * -1;
		}




		
	}

	
	return 0;

}