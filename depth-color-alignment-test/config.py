import depthai as dai

COLOR = True 		# Use color camera of mono camera

# DEPTH CONFIG
lrcheck  = True   			# Better handling for occlusions
extended = False  			# Closer-in minimum depth, disparity range is doubled
subpixel = False   			# Better accuracy for longer distance, fractional disparity 32-levels
confidence_threshold = 255 	# 0-255, 255 = low confidence, 0 = high confidence
min_range = 100 			# mm
max_range = 2000			# mm

# Median filter
# Options: MEDIAN_OFF, KERNEL_3x3, KERNEL_5x5, KERNEL_7x7
median   = dai.StereoDepthProperties.MedianFilter.MEDIAN_OFF


rectangle_perimeter_mm = (148+208)*2