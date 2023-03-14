import numpy as np



#This is based on the amount of concepts that assignment has
# So the impact is if you have an assignment based just on 1 concept it will count for more
# Then one that has multiple concepts
def amount_conc(data,skills,scale):

    concs_grade = []  # all concept grades
    for i in range(len(data)-5): # this is the student
        concept_grade = [] # used for each concept
        for x in skills[0][0][0:]:
            #lets find all assignments with this concept
            marks = 0
            total = 0
            for j, y in enumerate(data[0,2:]): # This is the assignment
                num_skill = y.count(',') + 1
                #y = ' '.join(y)
                weighting = 1- min(num_skill,6)/(53*(scale**2.4))  #0.5 aggressive 1 almost none
                if x in y and not isinstance(data[i+5,j+2],str):  # if excused do not include, our concept is in this assignment
                    marks += weighting*float(data[i+5,j+2])*float(data[2,j+2])
                    total += weighting*float(data[4,j+2])*float(data[2,j+2])
            
            if marks == marks: # do not if NaN
                concept_grade.append(round(100*marks/(total+0.001),1))
    
        concs_grade.append(concept_grade)
    # here we are making a list of each students list of concept grades

    return concs_grade
#This is the same as abouve but it puts more weight on the newer assignments in each concept
def time_amount_conc(num_skill,data,skills,scale,new_old):
    skill_weighting = []
    
    if new_old == 'new':
        for x in num_skill:
            skill_weighting.append(np.linspace(1,scale-0.001,x))
    else:
        for x in num_skill:
            skill_weighting.append(np.linspace(scale-0.001,1,x))

    concs_grade = []  # all concept grades
    for i in range(len(data)-5):# this is the student
        concept_grade = [] # used for each concept
        m = -1
        for x in skills[0][0][0:]:
            #lets find all assignments with this concept
            marks = 0
            total = 0
            n =-1
            m +=1
            for j, y in enumerate(data[0,2:]): # This is the assignment
                nums = y.count(',') + 1
                #y = ' '.join(y)
                weighting = 1- nums/(53*(scale**2.4))
                if x in y and not isinstance(data[i+5,j+2],str): # then our concept is in this assignment
                    n +=1
                    
                    marks += weighting*skill_weighting[m][n]*float(data[5+i,j+2])*float(data[2,j+2])
                    total += weighting*skill_weighting[m][n]*float(data[4,j+2])*float(data[2,j+2])
        
            if marks == marks: # do not if NaN
                concept_grade.append(round(100*marks/(total+0.001),1))
        concs_grade.append(concept_grade) # here we are making a list of each students list of concept grades

    return concs_grade
#This one is like the one above but not based on number of concepts
def time_based_conc(num_skill,data,skills,scale,new_old):  #scale is how aggressive the scaling

    skill_weighting = []

    if new_old == 'new':
        for x in num_skill:
            skill_weighting.append(np.linspace(1,scale-0.001,x))
    else:
        for x in num_skill:
            skill_weighting.append(np.linspace(scale-0.001,1,x))

    concs_grade = []  # all concept grades
    for i in range(len(data)-5):# this is the student
        concept_grade = [] # used for each concept
        m = -1
        for x in skills[0][0][0:]:
            #lets find all assignments with this concept
            marks = 0
            total = 0
            n =-1
            m +=1
            for j, y in enumerate(data[0,2:]): # This is the assignment
                #y = ' '.join(y)
                
                if x in y and not isinstance(data[i+5,j+2],str): # then our concept is in this assignment

                    n +=1
                    marks += skill_weighting[m][n]*float(data[5+i,j+2])*float(data[2,j+2])
                    total += skill_weighting[m][n]*float(data[4,j+2])*float(data[2,j+2])

            if marks == marks: # do not if NaN
                concept_grade.append(round(100*marks/(total+0.001),1))

        concs_grade.append(concept_grade) # here we are making a list of each students list of concept grades

    return concs_grade

#No scaling
def average_conc(data,skills):

    concs_grade = []  # all concept grades
    for i in range(len(data)-5): # this is the student
        concept_grade = [] # used for each concept
        for x in skills[0][0][0:]:
            #lets find all assignments with this concept
            marks = 0
            total = 0
            for j, y in enumerate(data[0,2:]): # This is the assiggnment
                #y = ' '.join(y)
                if x in y and not isinstance(data[i+5,j+2],str): # then our concept is in this assignment

                    marks += float(data[i+5,j+2])*float(data[2,j+2])
                    total += float(data[4,j+2])*float(data[2,j+2])

            if marks == marks: # do not if NaN
                concept_grade.append(round(100*marks/(total+0.001),1))

        concs_grade.append(concept_grade)
		# here we are making a list of each students list of concept grades 
    return concs_grade



#No scaling
def average_cont(data, skills):
	conts_grade = []  # all concept grades
	for i in range(len(data)-5): # this is the student
		content_grade = [] # used for each concept
		for x in skills[1][0][0:]:
			#lets find all assignments with this concept
			marks = 0
			total = 0
			for j, y in enumerate(data[1,2:]): # This is the assiggnment
                #y = ' '.join(y)

				if x in y and not isinstance(data[i+5,j+2],str): # then our concept is in this assignment
					marks += float(data[i+5,j+2])*float(data[2,j+2]) 
					total += float(data[4,j+2])*float(data[2,j+2]) 

			if marks == marks: # do not if NaN
            			content_grade.append(round(100*marks/(total+0.0001),1))  
		conts_grade.append(content_grade) # here we are making a list of each students list of concept grades
	return conts_grade











