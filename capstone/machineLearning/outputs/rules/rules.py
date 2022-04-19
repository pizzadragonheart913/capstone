def findDecision(obj): #obj[0]: CRIM, obj[1]: ZN, obj[2]: INDUS, obj[3]: CHAS, obj[4]: NOX, obj[5]: RM, obj[6]: AGE, obj[7]: DIS, obj[8]: RAD, obj[9]: TAX, obj[10]: PTRATIO, obj[11]: B, obj[12]: LSTAT, obj[13]: CAT. MEDV
	# {"feature": "CAT. MEDV", "instances": 505, "metric_value": 3.597, "depth": 1}
	if obj[13]<=0:
		# {"feature": "LSTAT", "instances": 421, "metric_value": 1.544, "depth": 2}
		if obj[12]<=14.163610451306411:
			# {"feature": "RM", "instances": 239, "metric_value": 0.3542, "depth": 3}
			if obj[5]>6.2201589958159:
				# {"feature": "PTRATIO", "instances": 121, "metric_value": 0.2581, "depth": 4}
				if obj[10]<=20.0861209415438:
					# {"feature": "TAX", "instances": 93, "metric_value": 0.1725, "depth": 5}
					if obj[9]<=414.75647383370256:
						# {"feature": "INDUS", "instances": 89, "metric_value": 0.0861, "depth": 6}
						if obj[2]<=6.7714606741573045:
							# {"feature": "DIS", "instances": 58, "metric_value": 0.194, "depth": 7}
							if obj[7]>5.93386724137931:
								# {"feature": "AGE", "instances": 30, "metric_value": 0.2483, "depth": 8}
								if obj[6]>6.8:
									# {"feature": "ZN", "instances": 29, "metric_value": 0.2113, "depth": 9}
									if obj[1]>0.0:
										# {"feature": "NOX", "instances": 28, "metric_value": 0.1854, "depth": 10}
										if obj[4]>0.389:
											# {"feature": "CRIM", "instances": 26, "metric_value": 0.298, "depth": 11}
											if obj[0]>0.01439:
												# {"feature": "B", "instances": 25, "metric_value": 0.1161, "depth": 12}
												if obj[11]>371.58:
													# {"feature": "RAD", "instances": 22, "metric_value": 0.0699, "depth": 13}
													if obj[8]>5:
														# {"feature": "CHAS", "instances": 14, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 22.2
														else: return 23.542857142857144
													elif obj[8]<=5:
														# {"feature": "CHAS", "instances": 8, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 25.0
														else: return 24.3875
													else: return 24.3875
												elif obj[11]<=371.58:
													return 25.2
												else: return 25.2
											elif obj[0]<=0.01439:
												return 29.1
											else: return 29.1
										elif obj[4]<=0.389:
											return 21.05
										else: return 21.05
									elif obj[1]<=0.0:
										return 28.7
									else: return 28.7
								elif obj[6]<=6.8:
									return 29.6
								else: return 29.6
							elif obj[7]<=5.93386724137931:
								# {"feature": "B", "instances": 28, "metric_value": 0.3332, "depth": 8}
								if obj[11]>391.7:
									# {"feature": "AGE", "instances": 19, "metric_value": 0.479, "depth": 9}
									if obj[6]>32.1:
										# {"feature": "CRIM", "instances": 16, "metric_value": 0.3396, "depth": 10}
										if obj[0]>0.03932:
											# {"feature": "ZN", "instances": 11, "metric_value": 0.5426, "depth": 11}
											if obj[1]<=25.0:
												# {"feature": "NOX", "instances": 9, "metric_value": 0.1996, "depth": 12}
												if obj[4]<=0.489:
													# {"feature": "RAD", "instances": 7, "metric_value": 0.0678, "depth": 13}
													if obj[8]>2:
														return 25.6
													elif obj[8]<=2:
														return 24.96666666666667
													else: return 24.96666666666667
												elif obj[4]>0.489:
													return 24.1
												else: return 24.1
											elif obj[1]>25.0:
												return 28.299999999999997
											else: return 28.299999999999997
										elif obj[0]<=0.03932:
											# {"feature": "NOX", "instances": 5, "metric_value": 0.3572, "depth": 11}
											if obj[4]>0.426:
												return 22.975
											elif obj[4]<=0.426:
												return 24.8
											else: return 24.8
										else: return 23.339999999999996
									elif obj[6]<=32.1:
										return 28.5
									else: return 28.5
								elif obj[11]<=391.7:
									# {"feature": "RAD", "instances": 9, "metric_value": 0.6152, "depth": 9}
									if obj[8]>5:
										# {"feature": "CRIM", "instances": 5, "metric_value": 0.264, "depth": 10}
										if obj[0]>0.35809:
											return 27.2
										elif obj[0]<=0.35809:
											return 26.549999999999997
										else: return 26.549999999999997
									elif obj[8]<=5:
										return 29.374999999999996
									else: return 29.374999999999996
								else: return 28.022222222222226
							else: return 26.303571428571427
						elif obj[2]>6.7714606741573045:
							# {"feature": "DIS", "instances": 31, "metric_value": 0.1341, "depth": 7}
							if obj[7]<=5.264927686329587:
								# {"feature": "AGE", "instances": 24, "metric_value": 0.2167, "depth": 8}
								if obj[6]>40.496222239001824:
									# {"feature": "NOX", "instances": 20, "metric_value": 0.335, "depth": 9}
									if obj[4]<=0.544:
										# {"feature": "CRIM", "instances": 14, "metric_value": 0.4773, "depth": 10}
										if obj[0]>0.10153:
											# {"feature": "B", "instances": 8, "metric_value": 0.3505, "depth": 11}
											if obj[11]>393.39:
												# {"feature": "ZN", "instances": 7, "metric_value": 0.1275, "depth": 12}
												if obj[1]<=0.0:
													# {"feature": "RAD", "instances": 6, "metric_value": 0.0164, "depth": 13}
													if obj[8]<=4:
														return 23.525
													elif obj[8]>4:
														return 23.450000000000003
													else: return 23.450000000000003
												elif obj[1]>0.0:
													return 24.4
												else: return 24.4
											elif obj[11]<=393.39:
												return 21.6
											else: return 21.6
										elif obj[0]<=0.10153:
											# {"feature": "B", "instances": 6, "metric_value": 0.2673, "depth": 11}
											if obj[11]>373.66:
												# {"feature": "ZN", "instances": 5, "metric_value": 0.1999, "depth": 12}
												if obj[1]<=0.0:
													return 21.400000000000002
												elif obj[1]>0.0:
													return 21.75
												else: return 21.75
											elif obj[11]<=373.66:
												return 20.0
											else: return 20.0
										else: return 21.28333333333333
									elif obj[4]>0.544:
										# {"feature": "CRIM", "instances": 6, "metric_value": 0.9732, "depth": 10}
										if obj[0]>0.07013:
											# {"feature": "CHAS", "instances": 5, "metric_value": 0.4597, "depth": 11}
											if obj[3]<=0:
												return 23.133333333333336
											elif obj[3]>0:
												return 25.0
											else: return 25.0
										elif obj[0]<=0.07013:
											return 28.7
										else: return 28.7
									else: return 24.683333333333334
								elif obj[6]<=40.496222239001824:
									return 25.6
								else: return 25.6
							elif obj[7]>5.264927686329587:
								# {"feature": "AGE", "instances": 7, "metric_value": 0.8314, "depth": 8}
								if obj[6]<=28.9:
									# {"feature": "RAD", "instances": 5, "metric_value": 0.7488, "depth": 9}
									if obj[8]>3:
										return 23.799999999999997
									elif obj[8]<=3:
										return 26.6
									else: return 26.6
								elif obj[6]>28.9:
									return 27.85
								else: return 27.85
							else: return 25.357142857142854
						else: return 23.95806451612903
					elif obj[9]>414.75647383370256:
						return 20.1
					else: return 20.1
				elif obj[10]>20.0861209415438:
					# {"feature": "AGE", "instances": 28, "metric_value": 0.3992, "depth": 5}
					if obj[6]>80.65:
						# {"feature": "CRIM", "instances": 17, "metric_value": 0.5313, "depth": 6}
						if obj[0]<=14.3337:
							# {"feature": "DIS", "instances": 16, "metric_value": 0.4006, "depth": 7}
							if obj[7]<=2.5182:
								# {"feature": "B", "instances": 10, "metric_value": 0.2912, "depth": 8}
								if obj[11]<=393.45:
									# {"feature": "NOX", "instances": 6, "metric_value": 0.2851, "depth": 9}
									if obj[4]<=0.718:
										return 22.075
									elif obj[4]>0.718:
										return 23.35
									else: return 23.35
								elif obj[11]>393.45:
									return 20.625
								else: return 20.625
							elif obj[7]>2.5182:
								# {"feature": "NOX", "instances": 6, "metric_value": 0.1761, "depth": 8}
								if obj[4]>0.52:
									# {"feature": "B", "instances": 5, "metric_value": 0.3374, "depth": 9}
									if obj[11]>380.23:
										return 19.424999999999997
									elif obj[11]<=380.23:
										return 21.0
									else: return 21.0
								elif obj[4]<=0.52:
									return 18.6
								else: return 18.6
							else: return 19.55
						elif obj[0]>14.3337:
							return 15.0
						else: return 15.0
					elif obj[6]<=80.65:
						# {"feature": "CRIM", "instances": 11, "metric_value": 0.9972, "depth": 6}
						if obj[0]<=5.82401:
							# {"feature": "DIS", "instances": 10, "metric_value": 0.9739, "depth": 7}
							if obj[7]<=3.4106:
								# {"feature": "NOX", "instances": 6, "metric_value": 0.9149, "depth": 8}
								if obj[4]<=0.573:
									# {"feature": "INDUS", "instances": 5, "metric_value": 1.0042, "depth": 9}
									if obj[2]>8.56:
										return 23.7
									elif obj[2]<=8.56:
										return 27.0
									else: return 27.0
								elif obj[4]>0.573:
									return 29.8
								else: return 29.8
							elif obj[7]>3.4106:
								return 21.775000000000002
							else: return 21.775000000000002
						elif obj[0]>5.82401:
							return 16.1
						else: return 16.1
					else: return 23.46363636363636
				else: return 21.71071428571429
			elif obj[5]<=6.2201589958159:
				# {"feature": "TAX", "instances": 118, "metric_value": 0.1684, "depth": 4}
				if obj[9]>193:
					# {"feature": "DIS", "instances": 116, "metric_value": 0.0984, "depth": 5}
					if obj[7]>1.2852:
						# {"feature": "CRIM", "instances": 115, "metric_value": 0.0756, "depth": 6}
						if obj[0]<=16.626807544558:
							# {"feature": "B", "instances": 114, "metric_value": 0.0673, "depth": 7}
							if obj[11]>271.5269646287531:
								# {"feature": "AGE", "instances": 111, "metric_value": 0.0551, "depth": 8}
								if obj[6]>30.31845719771557:
									# {"feature": "RAD", "instances": 92, "metric_value": 0.0645, "depth": 9}
									if obj[8]<=6:
										# {"feature": "ZN", "instances": 75, "metric_value": 0.0616, "depth": 10}
										if obj[1]<=12.5:
											# {"feature": "PTRATIO", "instances": 64, "metric_value": 0.078, "depth": 11}
											if obj[10]>18.6109375:
												# {"feature": "INDUS", "instances": 35, "metric_value": 0.1601, "depth": 12}
												if obj[2]<=8.14:
													# {"feature": "NOX", "instances": 23, "metric_value": 0.0638, "depth": 13}
													if obj[4]>0.442:
														# {"feature": "CHAS", "instances": 19, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 20.4
														else: return 19.442105263157895
													elif obj[4]<=0.442:
														return 18.25
													else: return 18.25
												elif obj[2]>8.14:
													# {"feature": "NOX", "instances": 12, "metric_value": 0.2155, "depth": 13}
													if obj[4]<=0.573:
														# {"feature": "CHAS", "instances": 7, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 20.8
														else: return 20.45714285714286
													elif obj[4]>0.573:
														# {"feature": "CHAS", "instances": 5, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 20.1
														else: return 21.18
													else: return 21.18
												else: return 20.758333333333333
											elif obj[10]<=18.6109375:
												# {"feature": "NOX", "instances": 29, "metric_value": 0.175, "depth": 12}
												if obj[4]>0.51:
													# {"feature": "INDUS", "instances": 18, "metric_value": 0.095, "depth": 13}
													if obj[2]<=10.01:
														# {"feature": "CHAS", "instances": 11, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 22.9
														else: return 19.69090909090909
													elif obj[2]>10.01:
														# {"feature": "CHAS", "instances": 7, "metric_value": 0.3362, "depth": 14}
														if obj[3]<=0:
															return 21.5
														elif obj[3]>0:
															return 15.3
														else: return 19.3
													else: return 20.82857142857143
												elif obj[4]<=0.51:
													# {"feature": "INDUS", "instances": 11, "metric_value": 0.2062, "depth": 13}
													if obj[2]<=6.91:
														# {"feature": "CHAS", "instances": 9, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 21.2
														else: return 21.355555555555554
													elif obj[2]>6.91:
														return 23.35
													else: return 23.35
												else: return 21.718181818181815
											else: return 20.73448275862069
										elif obj[1]>12.5:
											# {"feature": "PTRATIO", "instances": 11, "metric_value": 0.3418, "depth": 11}
											if obj[10]>14.7:
												# {"feature": "NOX", "instances": 9, "metric_value": 0.3429, "depth": 12}
												if obj[4]>0.426:
													# {"feature": "INDUS", "instances": 5, "metric_value": 0.2074, "depth": 13}
													if obj[2]<=5.64:
														return 20.1
													elif obj[2]>5.64:
														return 20.9
													else: return 20.9
												elif obj[4]<=0.426:
													return 21.849999999999998
												else: return 21.849999999999998
											elif obj[10]<=14.7:
												return 23.450000000000003
											else: return 23.450000000000003
										else: return 21.49090909090909
									elif obj[8]>6:
										# {"feature": "PTRATIO", "instances": 17, "metric_value": 0.2904, "depth": 10}
										if obj[10]>17.4:
											# {"feature": "NOX", "instances": 15, "metric_value": 0.3664, "depth": 11}
											if obj[4]<=0.655:
												# {"feature": "ZN", "instances": 10, "metric_value": 0.3403, "depth": 12}
												if obj[1]<=0.0:
													# {"feature": "INDUS", "instances": 6, "metric_value": 0.0, "depth": 13}
													if obj[2]<=18.1:
														# {"feature": "CHAS", "instances": 6, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 20.6
														else: return 20.849999999999998
													else: return 20.849999999999998
												elif obj[1]>0.0:
													return 20.05
												else: return 20.05
											elif obj[4]>0.655:
												# {"feature": "CHAS", "instances": 5, "metric_value": 0.2508, "depth": 12}
												if obj[3]<=0:
													return 23.200000000000003
												elif obj[3]>0:
													return 22.7
												else: return 22.7
											else: return 23.1
										elif obj[10]<=17.4:
											return 24.15
										else: return 24.15
									else: return 21.711764705882356
								elif obj[6]<=30.31845719771557:
									# {"feature": "ZN", "instances": 19, "metric_value": 0.9229, "depth": 9}
									if obj[1]<=28.0:
										# {"feature": "INDUS", "instances": 13, "metric_value": 0.5224, "depth": 10}
										if obj[2]>3.24:
											# {"feature": "NOX", "instances": 12, "metric_value": 0.3453, "depth": 11}
											if obj[4]>0.413:
												# {"feature": "RAD", "instances": 9, "metric_value": 0.207, "depth": 12}
												if obj[8]>3:
													# {"feature": "PTRATIO", "instances": 7, "metric_value": 0.1558, "depth": 13}
													if obj[10]<=19.2:
														# {"feature": "CHAS", "instances": 5, "metric_value": 0.0, "depth": 14}
														if obj[3]<=0:
															return 24.7
														else: return 23.919999999999998
													elif obj[10]>19.2:
														return 23.200000000000003
													else: return 23.200000000000003
												elif obj[8]<=3:
													return 25.0
												else: return 25.0
											elif obj[4]<=0.413:
												return 22.166666666666668
											else: return 22.166666666666668
										elif obj[2]<=3.24:
											return 19.3
										else: return 19.3
									elif obj[1]>28.0:
										# {"feature": "NOX", "instances": 6, "metric_value": 0.3532, "depth": 10}
										if obj[4]>0.392:
											# {"feature": "INDUS", "instances": 5, "metric_value": 0.127, "depth": 11}
											if obj[2]>1.69:
												return 18.825000000000003
											elif obj[2]<=1.69:
												return 18.6
											else: return 18.6
										elif obj[4]<=0.392:
											return 20.9
										else: return 20.9
									else: return 19.133333333333336
								else: return 21.926315789473687
							elif obj[11]<=271.5269646287531:
								return 23.96666666666667
							else: return 23.96666666666667
						elif obj[0]>16.626807544558:
							return 15.0
						else: return 15.0
					elif obj[7]<=1.2852:
						return 27.9
					else: return 27.9
				elif obj[9]<=193:
					return 28.0
				else: return 28.0
			else: return 21.065254237288134
		elif obj[12]>14.163610451306411:
			# {"feature": "CRIM", "instances": 182, "metric_value": 0.7255, "depth": 3}
			if obj[0]<=8.162174560439563:
				# {"feature": "AGE", "instances": 116, "metric_value": 0.3922, "depth": 4}
				if obj[6]>73.60099458825695:
					# {"feature": "TAX", "instances": 101, "metric_value": 0.1997, "depth": 5}
					if obj[9]>304:
						# {"feature": "RM", "instances": 86, "metric_value": 0.241, "depth": 6}
						if obj[5]>5.544901443306964:
							# {"feature": "B", "instances": 73, "metric_value": 0.2634, "depth": 7}
							if obj[11]>322.03534246575344:
								# {"feature": "RAD", "instances": 48, "metric_value": 0.3489, "depth": 8}
								if obj[8]>4:
									# {"feature": "NOX", "instances": 29, "metric_value": 0.3807, "depth": 9}
									if obj[4]<=0.584:
										# {"feature": "DIS", "instances": 15, "metric_value": 0.5821, "depth": 10}
										if obj[7]>2.548:
											# {"feature": "ZN", "instances": 8, "metric_value": 0.4484, "depth": 11}
											if obj[1]>0.0:
												return 19.375
											elif obj[1]<=0.0:
												return 20.975
											else: return 20.975
										elif obj[7]<=2.548:
											# {"feature": "INDUS", "instances": 7, "metric_value": 0.2434, "depth": 11}
											if obj[2]>8.56:
												return 18.725
											elif obj[2]<=8.56:
												return 19.466666666666665
											else: return 19.466666666666665
										else: return 19.042857142857144
									elif obj[4]>0.584:
										# {"feature": "DIS", "instances": 14, "metric_value": 0.9439, "depth": 10}
										if obj[7]>1.6768:
											# {"feature": "CHAS", "instances": 11, "metric_value": 0.1288, "depth": 11}
											if obj[3]<=0:
												# {"feature": "INDUS", "instances": 10, "metric_value": 0.1506, "depth": 12}
												if obj[2]>9.69:
													# {"feature": "ZN", "instances": 9, "metric_value": 0.0, "depth": 13}
													if obj[1]<=0.0:
														# {"feature": "PTRATIO", "instances": 9, "metric_value": 0.0, "depth": 14}
														if obj[10]<=20.2:
															return 19.9
														else: return 18.03333333333333
													else: return 18.03333333333333
												elif obj[2]<=9.69:
													return 16.8
												else: return 16.8
											elif obj[3]>0:
												return 16.8
											else: return 16.8
										elif obj[7]<=1.6768:
											return 12.133333333333333
										else: return 12.133333333333333
									else: return 16.592857142857138
								elif obj[8]<=4:
									# {"feature": "NOX", "instances": 19, "metric_value": 0.2174, "depth": 9}
									if obj[4]>0.609:
										# {"feature": "DIS", "instances": 10, "metric_value": 0.73, "depth": 10}
										if obj[7]>1.6686:
											# {"feature": "ZN", "instances": 8, "metric_value": 0.0, "depth": 11}
											if obj[1]<=0.0:
												# {"feature": "INDUS", "instances": 8, "metric_value": 0.0, "depth": 12}
												if obj[2]<=21.89:
													# {"feature": "CHAS", "instances": 8, "metric_value": 0.0, "depth": 13}
													if obj[3]<=0:
														# {"feature": "PTRATIO", "instances": 8, "metric_value": 0.0, "depth": 14}
														if obj[10]<=21.2:
															return 16.2
														else: return 17.1625
													else: return 17.1625
												else: return 17.1625
											else: return 17.1625
										elif obj[7]<=1.6686:
											return 13.65
										else: return 13.65
									elif obj[4]<=0.609:
										# {"feature": "DIS", "instances": 9, "metric_value": 0.7283, "depth": 10}
										if obj[7]<=4.233:
											# {"feature": "INDUS", "instances": 6, "metric_value": 0.0768, "depth": 11}
											if obj[2]<=8.14:
												# {"feature": "ZN", "instances": 5, "metric_value": 0.0, "depth": 12}
												if obj[1]<=0.0:
													# {"feature": "CHAS", "instances": 5, "metric_value": 0.0, "depth": 13}
													if obj[3]<=0:
														# {"feature": "PTRATIO", "instances": 5, "metric_value": 0.0, "depth": 14}
														if obj[10]<=21.0:
															return 13.6
														else: return 13.819999999999999
													else: return 13.819999999999999
												else: return 13.819999999999999
											elif obj[2]>8.14:
												return 13.6
											else: return 13.6
										elif obj[7]>4.233:
											return 16.566666666666666
										else: return 16.566666666666666
									else: return 14.711111111111112
								else: return 15.631578947368425
							elif obj[11]<=322.03534246575344:
								# {"feature": "INDUS", "instances": 25, "metric_value": 0.2313, "depth": 8}
								if obj[2]<=18.1:
									# {"feature": "DIS", "instances": 18, "metric_value": 0.1933, "depth": 9}
									if obj[7]>1.4547:
										# {"feature": "NOX", "instances": 17, "metric_value": 0.1831, "depth": 10}
										if obj[4]>0.614:
											# {"feature": "ZN", "instances": 11, "metric_value": 0.0, "depth": 11}
											if obj[1]<=0.0:
												# {"feature": "CHAS", "instances": 11, "metric_value": 0.0, "depth": 12}
												if obj[3]<=0:
													# {"feature": "RAD", "instances": 11, "metric_value": 0.0, "depth": 13}
													if obj[8]<=24:
														# {"feature": "PTRATIO", "instances": 11, "metric_value": 0.0, "depth": 14}
														if obj[10]<=20.2:
															return 14.9
														else: return 14.354545454545455
													else: return 14.354545454545455
												else: return 14.354545454545455
											else: return 14.354545454545455
										elif obj[4]<=0.614:
											# {"feature": "RAD", "instances": 6, "metric_value": 0.1279, "depth": 11}
											if obj[8]<=4:
												return 13.850000000000001
											elif obj[8]>4:
												return 13.350000000000001
											else: return 13.350000000000001
										else: return 13.683333333333335
									elif obj[7]<=1.4547:
										return 17.2
									else: return 17.2
								elif obj[2]>18.1:
									# {"feature": "DIS", "instances": 7, "metric_value": 0.463, "depth": 9}
									if obj[7]>1.4191:
										# {"feature": "RAD", "instances": 6, "metric_value": 0.2138, "depth": 10}
										if obj[8]>4:
											# {"feature": "CHAS", "instances": 5, "metric_value": 0.1916, "depth": 11}
											if obj[3]<=0:
												return 17.466666666666665
											elif obj[3]>0:
												return 16.3
											else: return 16.3
										elif obj[8]<=4:
											return 15.6
										else: return 15.6
									elif obj[7]<=1.4191:
										return 13.8
									else: return 13.8
								else: return 16.342857142857145
							else: return 14.864
						elif obj[5]<=5.544901443306964:
							# {"feature": "B", "instances": 13, "metric_value": 0.8136, "depth": 7}
							if obj[11]>344.05:
								# {"feature": "INDUS", "instances": 10, "metric_value": 0.3308, "depth": 8}
								if obj[2]>18.1:
									# {"feature": "DIS", "instances": 7, "metric_value": 0.6286, "depth": 9}
									if obj[7]>1.3459:
										# {"feature": "NOX", "instances": 5, "metric_value": 0.2552, "depth": 10}
										if obj[4]>0.624:
											return 16.0
										elif obj[4]<=0.624:
											return 14.8
										else: return 14.8
									elif obj[7]<=1.3459:
										return 12.600000000000001
									else: return 12.600000000000001
								elif obj[2]<=18.1:
									return 12.533333333333333
								else: return 12.533333333333333
							elif obj[11]<=344.05:
								return 9.4
							else: return 9.4
						else: return 12.96923076923077
					elif obj[9]<=304:
						# {"feature": "NOX", "instances": 15, "metric_value": 0.6776, "depth": 6}
						if obj[4]>0.453:
							# {"feature": "DIS", "instances": 12, "metric_value": 0.6554, "depth": 7}
							if obj[7]>1.9444:
								# {"feature": "INDUS", "instances": 10, "metric_value": 0.3559, "depth": 8}
								if obj[2]>4.05:
									# {"feature": "RM", "instances": 9, "metric_value": 0.5771, "depth": 9}
									if obj[5]>5.914:
										# {"feature": "B", "instances": 5, "metric_value": 0.4523, "depth": 10}
										if obj[11]>378.09:
											return 21.53333333333333
										elif obj[11]<=378.09:
											return 20.4
										else: return 20.4
									elif obj[5]<=5.914:
										return 18.974999999999998
									else: return 18.974999999999998
								elif obj[2]<=4.05:
									return 23.1
								else: return 23.1
							elif obj[7]<=1.9444:
								return 16.5
							else: return 16.5
						elif obj[4]<=0.453:
							return 15.666666666666666
						else: return 15.666666666666666
					else: return 18.96
				elif obj[6]<=73.60099458825695:
					# {"feature": "B", "instances": 15, "metric_value": 0.6122, "depth": 5}
					if obj[11]<=393.29:
						# {"feature": "ZN", "instances": 9, "metric_value": 0.6418, "depth": 6}
						if obj[1]<=12.5:
							# {"feature": "TAX", "instances": 8, "metric_value": 0.3779, "depth": 7}
							if obj[9]<=391:
								# {"feature": "RM", "instances": 7, "metric_value": 0.3186, "depth": 8}
								if obj[5]<=5.889:
									# {"feature": "INDUS", "instances": 6, "metric_value": 0.1714, "depth": 9}
									if obj[2]>7.87:
										# {"feature": "DIS", "instances": 5, "metric_value": 0.1782, "depth": 10}
										if obj[7]>2.2577:
											return 22.924999999999997
										elif obj[7]<=2.2577:
											return 22.0
										else: return 22.0
									elif obj[2]<=7.87:
										return 21.7
									else: return 21.7
								elif obj[5]>5.889:
									return 24.4
								else: return 24.4
							elif obj[9]>391:
								return 20.4
							else: return 20.4
						elif obj[1]>12.5:
							return 18.5
						else: return 18.5
					elif obj[11]>393.29:
						# {"feature": "DIS", "instances": 6, "metric_value": 0.5105, "depth": 6}
						if obj[7]>2.3999:
							# {"feature": "INDUS", "instances": 5, "metric_value": 0.2047, "depth": 7}
							if obj[2]>6.91:
								return 19.933333333333334
							elif obj[2]<=6.91:
								return 19.15
							else: return 19.15
						elif obj[7]<=2.3999:
							return 17.5
						else: return 17.5
					else: return 19.266666666666666
				else: return 20.953333333333333
			elif obj[0]>8.162174560439563:
				# {"feature": "NOX", "instances": 66, "metric_value": 0.6352, "depth": 4}
				if obj[4]>0.597:
					# {"feature": "DIS", "instances": 56, "metric_value": 0.4131, "depth": 5}
					if obj[7]<=2.1033242447390936:
						# {"feature": "B", "instances": 47, "metric_value": 0.2404, "depth": 6}
						if obj[11]>131.53643751944344:
							# {"feature": "AGE", "instances": 34, "metric_value": 0.2931, "depth": 7}
							if obj[6]>91.2:
								# {"feature": "RM", "instances": 30, "metric_value": 0.1728, "depth": 8}
								if obj[5]>5.793233333333335:
									# {"feature": "ZN", "instances": 17, "metric_value": 0.0, "depth": 9}
									if obj[1]<=0.0:
										# {"feature": "INDUS", "instances": 17, "metric_value": 0.0, "depth": 10}
										if obj[2]<=18.1:
											# {"feature": "CHAS", "instances": 17, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "RAD", "instances": 17, "metric_value": 0.0, "depth": 12}
												if obj[8]<=24:
													# {"feature": "TAX", "instances": 17, "metric_value": 0.0, "depth": 13}
													if obj[9]<=666:
														# {"feature": "PTRATIO", "instances": 17, "metric_value": 0.0, "depth": 14}
														if obj[10]<=20.2:
															return 13.1
														else: return 12.164705882352942
													else: return 12.164705882352942
												else: return 12.164705882352942
											else: return 12.164705882352942
										else: return 12.164705882352942
									else: return 12.164705882352942
								elif obj[5]<=5.793233333333335:
									# {"feature": "ZN", "instances": 13, "metric_value": 0.0, "depth": 9}
									if obj[1]<=0.0:
										# {"feature": "INDUS", "instances": 13, "metric_value": 0.0, "depth": 10}
										if obj[2]<=18.1:
											# {"feature": "CHAS", "instances": 13, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "RAD", "instances": 13, "metric_value": 0.0, "depth": 12}
												if obj[8]<=24:
													# {"feature": "TAX", "instances": 13, "metric_value": 0.0, "depth": 13}
													if obj[9]<=666:
														# {"feature": "PTRATIO", "instances": 13, "metric_value": 0.0, "depth": 14}
														if obj[10]<=20.2:
															return 13.8
														else: return 10.115384615384615
													else: return 10.115384615384615
												else: return 10.115384615384615
											else: return 10.115384615384615
										else: return 10.115384615384615
									else: return 10.115384615384615
								else: return 10.115384615384615
							elif obj[6]<=91.2:
								return 7.750000000000001
							else: return 7.750000000000001
						elif obj[11]<=131.53643751944344:
							# {"feature": "AGE", "instances": 13, "metric_value": 0.2076, "depth": 7}
							if obj[6]<=95.6:
								# {"feature": "RM", "instances": 9, "metric_value": 0.3033, "depth": 8}
								if obj[5]<=6.461:
									# {"feature": "ZN", "instances": 7, "metric_value": 0.0, "depth": 9}
									if obj[1]<=0.0:
										# {"feature": "INDUS", "instances": 7, "metric_value": 0.0, "depth": 10}
										if obj[2]<=18.1:
											# {"feature": "CHAS", "instances": 7, "metric_value": 0.0, "depth": 11}
											if obj[3]<=0:
												# {"feature": "RAD", "instances": 7, "metric_value": 0.0, "depth": 12}
												if obj[8]<=24:
													# {"feature": "TAX", "instances": 7, "metric_value": 0.0, "depth": 13}
													if obj[9]<=666:
														# {"feature": "PTRATIO", "instances": 7, "metric_value": 0.0, "depth": 14}
														if obj[10]<=20.2:
															return 10.4
														else: return 9.842857142857143
													else: return 9.842857142857143
												else: return 9.842857142857143
											else: return 9.842857142857143
										else: return 9.842857142857143
									else: return 9.842857142857143
								elif obj[5]>6.461:
									return 7.95
								else: return 7.95
							elif obj[6]>95.6:
								return 7.925
							else: return 7.925
						else: return 8.961538461538462
					elif obj[7]>2.1033242447390936:
						# {"feature": "AGE", "instances": 9, "metric_value": 0.6811, "depth": 6}
						if obj[6]<=96.7:
							# {"feature": "RM", "instances": 6, "metric_value": 0.2893, "depth": 7}
							if obj[5]<=6.629:
								# {"feature": "B", "instances": 5, "metric_value": 0.1393, "depth": 8}
								if obj[11]<=379.7:
									return 13.3
								elif obj[11]>379.7:
									return 12.6
								else: return 12.6
							elif obj[5]>6.629:
								return 14.9
							else: return 14.9
						elif obj[6]>96.7:
							return 16.566666666666666
						else: return 16.566666666666666
					else: return 14.488888888888889
				elif obj[4]<=0.597:
					# {"feature": "RM", "instances": 10, "metric_value": 1.8063, "depth": 5}
					if obj[5]<=6.833:
						# {"feature": "B", "instances": 9, "metric_value": 1.3607, "depth": 6}
						if obj[11]>24.65:
							# {"feature": "AGE", "instances": 7, "metric_value": 0.8684, "depth": 7}
							if obj[6]>71.0:
								# {"feature": "DIS", "instances": 5, "metric_value": 1.0103, "depth": 8}
								if obj[7]<=1.5894:
									return 17.13333333333333
								elif obj[7]>1.5894:
									return 14.3
								else: return 14.3
							elif obj[6]<=71.0:
								return 19.6
							else: return 19.6
						elif obj[11]<=24.65:
							return 10.95
						else: return 10.95
					elif obj[5]>6.833:
						return 27.5
					else: return 27.5
				else: return 16.86
			else: return 11.890909090909092
		else: return 15.097252747252746
	elif obj[13]>0:
		# {"feature": "RM", "instances": 84, "metric_value": 1.308, "depth": 2}
		if obj[5]<=7.293523809523809:
			# {"feature": "CRIM", "instances": 49, "metric_value": 3.2317, "depth": 3}
			if obj[0]<=2.9769150682521266:
				# {"feature": "INDUS", "instances": 44, "metric_value": 0.3115, "depth": 4}
				if obj[2]<=9.735269181893411:
					# {"feature": "TAX", "instances": 43, "metric_value": 0.2749, "depth": 5}
					if obj[9]>245:
						# {"feature": "DIS", "instances": 29, "metric_value": 0.1666, "depth": 6}
						if obj[7]>1.9301:
							# {"feature": "NOX", "instances": 28, "metric_value": 0.1878, "depth": 7}
							if obj[4]<=0.447:
								# {"feature": "ZN", "instances": 21, "metric_value": 0.1755, "depth": 8}
								if obj[1]>40.0:
									# {"feature": "LSTAT", "instances": 15, "metric_value": 0.2881, "depth": 9}
									if obj[12]>2.87:
										# {"feature": "B", "instances": 13, "metric_value": 0.279, "depth": 10}
										if obj[11]<=395.63:
											# {"feature": "AGE", "instances": 10, "metric_value": 0.2165, "depth": 11}
											if obj[6]>21.5:
												# {"feature": "RAD", "instances": 6, "metric_value": 0.3368, "depth": 12}
												if obj[8]>2:
													return 31.225
												elif obj[8]<=2:
													return 32.45
												else: return 32.45
											elif obj[6]<=21.5:
												return 33.3
											else: return 33.3
										elif obj[11]>395.63:
											return 34.36666666666667
										else: return 34.36666666666667
									elif obj[12]<=2.87:
										return 35.65
									else: return 35.65
								elif obj[1]<=40.0:
									# {"feature": "B", "instances": 6, "metric_value": 0.268, "depth": 9}
									if obj[11]>393.45:
										return 32.36666666666667
									elif obj[11]<=393.45:
										return 33.13333333333333
									else: return 33.13333333333333
								else: return 32.75
							elif obj[4]>0.447:
								# {"feature": "LSTAT", "instances": 7, "metric_value": 0.254, "depth": 8}
								if obj[12]<=7.6:
									# {"feature": "AGE", "instances": 5, "metric_value": 0.5644, "depth": 9}
									if obj[6]<=79.9:
										return 31.433333333333334
									elif obj[6]>79.9:
										return 30.1
									else: return 30.1
								elif obj[12]>7.6:
									return 32.25
								else: return 32.25
							else: return 31.285714285714285
						elif obj[7]<=1.9301:
							return 36.5
						else: return 36.5
					elif obj[9]<=245:
						# {"feature": "DIS", "instances": 14, "metric_value": 0.5744, "depth": 6}
						if obj[7]<=9.2229:
							# {"feature": "AGE", "instances": 13, "metric_value": 0.2916, "depth": 7}
							if obj[6]<=92.2:
								# {"feature": "NOX", "instances": 12, "metric_value": 0.3067, "depth": 8}
								if obj[4]<=0.469:
									# {"feature": "B", "instances": 8, "metric_value": 0.3979, "depth": 9}
									if obj[11]<=394.63:
										return 34.125
									elif obj[11]>394.63:
										return 36.0
									else: return 36.0
								elif obj[4]>0.469:
									return 36.85
								else: return 36.85
							elif obj[6]>92.2:
								return 32.5
							else: return 32.5
						elif obj[7]>9.2229:
							return 30.1
						else: return 30.1
					else: return 35.03571428571429
				elif obj[2]>9.735269181893411:
					return 41.3
				else: return 41.3
			elif obj[0]>2.9769150682521266:
				return 50.0
			else: return 50.0
		elif obj[5]>7.293523809523809:
			# {"feature": "LSTAT", "instances": 35, "metric_value": 1.1498, "depth": 3}
			if obj[12]<=4.548571428571428:
				# {"feature": "CRIM", "instances": 22, "metric_value": 0.7919, "depth": 4}
				if obj[0]<=1.079067634652554:
					# {"feature": "TAX", "instances": 18, "metric_value": 0.9654, "depth": 5}
					if obj[9]>255:
						# {"feature": "B", "instances": 10, "metric_value": 1.1069, "depth": 6}
						if obj[11]>385.05:
							# {"feature": "AGE", "instances": 7, "metric_value": 1.5211, "depth": 7}
							if obj[6]<=73.3:
								# {"feature": "DIS", "instances": 5, "metric_value": 0.438, "depth": 8}
								if obj[7]>3.4952:
									return 42.266666666666666
								elif obj[7]<=3.4952:
									return 43.65
								else: return 43.65
							elif obj[6]>73.3:
								return 38.150000000000006
							else: return 38.150000000000006
						elif obj[11]<=385.05:
							return 46.6
						else: return 46.6
					elif obj[9]<=255:
						# {"feature": "INDUS", "instances": 8, "metric_value": 1.6294, "depth": 6}
						if obj[2]<=2.68:
							# {"feature": "ZN", "instances": 5, "metric_value": 0.3, "depth": 7}
							if obj[1]<=90.0:
								return 50.0
							elif obj[1]>90.0:
								return 49.25
							else: return 49.25
						elif obj[2]>2.68:
							return 45.13333333333333
						else: return 45.13333333333333
					else: return 47.9875
				elif obj[0]>1.079067634652554:
					return 50.0
				else: return 50.0
			elif obj[12]>4.548571428571428:
				# {"feature": "DIS", "instances": 13, "metric_value": 2.7563, "depth": 4}
				if obj[7]<=2.8944:
					# {"feature": "CRIM", "instances": 8, "metric_value": 3.2574, "depth": 5}
					if obj[0]<=0.61154:
						# {"feature": "INDUS", "instances": 6, "metric_value": 1.7926, "depth": 6}
						if obj[2]>2.46:
							# {"feature": "AGE", "instances": 5, "metric_value": 1.5406, "depth": 7}
							if obj[6]<=86.9:
								return 50.0
							elif obj[6]>86.9:
								return 45.95
							else: return 45.95
						elif obj[2]<=2.46:
							return 39.8
						else: return 39.8
					elif obj[0]>0.61154:
						return 33.5
					else: return 33.5
				elif obj[7]>2.8944:
					# {"feature": "CRIM", "instances": 5, "metric_value": 0.7605, "depth": 5}
					if obj[0]<=0.22188:
						return 33.93333333333334
					elif obj[0]>0.22188:
						return 31.6
					else: return 31.6
				else: return 33.00000000000001
			else: return 39.51538461538461
		else: return 43.651428571428575
	else: return 38.79761904761905
