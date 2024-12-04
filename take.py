from superwires import games #made this change to use superwires instead of livewires 

games.init(screen_width = 1000, screen_height = 900, fps = 50) 
 
wall_image = games.load_image("sun.jpeg", transparent = False) 
games.screen.background = wall_image 
 
pizza_image = games.load_image("ty.jpeg") 
pizza = games.Sprite(image = pizza_image, x = 170, y = 620) #;locates the sprite in the middle of the program window 
games.screen.add(pizza) 
 
games.screen.mainloop() 