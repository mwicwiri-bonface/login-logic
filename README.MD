Start																									
	Call page																								
javascript		web app dowellclock(t1,t2,t3, IP, Language)																							
																									
			Select language																						
				List of language from language master based on city master set to (array)																					
				Mark user's browsing language																					
Python	Call dowelllogin () in home page																								
		Login form (No)																							
			go to 100																						
		Login form (yes)																							
			List of language in drop down menu from language array																						
			user name																						
				check frontend rules of user name																					
					call languagedetection ()																				
			password																						
				check pass word rules																					
			take Face ID/Selffie																						
			Take voice																						
		New user contact admin for user name and password																							
		If cancel																							
			exit																						
100		if login																							
javascript			permission for location (variable)																						
				call dowelllocation (permission yes/no)																					
				web app dowelllocation(IP, Latitude, Longitude, region, language, city, contry)																					
python			varify user																						
				If selffie (No)																					
					go to 110																				
				if selffie (yes)																					
				dowellconnection (insert, selfie)																					
				call dowellfaceID() Face ID/Selffie																					
					if yes																				
110					if voice (No)																				
						go to 120																			
					if voice (yes)																				
					dowellconnection (insert, voice)																				
					call dowelvoiceID ()																				
						if yes																			
120						Layer (1,2,3,4,5,6) based rights																			
							if yes																		
							Location based rights																		
								Regional > country > city wise rights of the project																	
								Connect to city master																	
								if yes																	
								Connectivity based rights																	
									If yes																
									Device based rights																
										If yes															
										OS based rights															
											If yes														
											role based rights														
												if yes													
												Process based rights													
													if yes												
													user based rights (edit, add, update, view)												
														Connect to user master											
														If yes											
														Login											
														set rights to array											
														Prompt (user rights)											
														Continue 200											
			if No																						
				Prompt ( Rights not set, contact admin)																					
																									
200	session ID																								
		create session ID																							
		user ID + Language ID + Session number																							
		web app call dowellconnection ()																							
		save to logedin queue																							
																									
		web app eventcreation ()																							
																									
	Cal result																								
		dowelllogin (sessionID, selffie ID, Voice ID, rights (array))																							
																									
End	