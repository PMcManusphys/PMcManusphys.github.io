# reportcard functions
from random import randrange

ie_cont = []
ie_cont.append([" has not yet demonstrated their understanding in", " have not yet demonstrated your understanding in"])
ie_cont.append([" has not met the minimum required understanding of"," have not met the minimum required understanding of"])
ie_cont.append([" is having a hard time grasping"," are having a hard grasping"])


emerging_cont = []
emerging_cont.append([" is beginning to understand"," are beginning to understand"])
emerging_cont.append([" is just starting to understand"," are just starting to understand"])
emerging_cont.append([" has partially met a few of the criteria of"," have partially met a few of the criteria of"])
emerging_cont.append([" needs more time to develop their understanding of"," need more time to develop your understanding of"])


dev_cont = []
dev_cont.append([", with prompting is able to show their understanding of"," can with prompting show their understanding of" ])
dev_cont.append([", in specific situations applies understanding of", " have in specific situations apply your understanding of"])
dev_cont.append([" has partially met some of the criteria of"," have partially met some of the criteria of"])

pro_cont = []
pro_cont.append([", in many situations, is able to apply their understanding of"," have in many situations, applied your understanding of"])
pro_cont.append([", can clearly communicate their understanding of"," can clearly communicate your understanding of"])
pro_cont.append([" has met the criteria of"," have met the criteria of"])
pro_cont.append([" has good insight into"," have good insight into"])
pro_cont.append([" demonstrates a clear understanding of"," demonstrate a clear understanding of"])


ext_cont = []
ext_cont.append([" shows in-depth understanding of"," show an in-depth understanding of"])
ext_cont.append([" has gone beyond the criteria of"," have gone beyond the criteria of"])
ext_cont.append([", in complex situations is able to show their understanding of"," can in complex situations show your understanding of"])

connecting = []
connecting.append(["and therefore is at a proficiency scale of","and therefore are at a proficiency scale of"])
connecting.append(["and is sitting at a proficiency scale of", "and are sitting at a proficiency scale of"])
connecting.append(["while having a proficiency scale of","while having a proficiency scale of"])

improving_com = []
improving_com.append("You started the course off strong, but had more trouble with the latest part of the course. ")
improving_com.append("The start of the course was your strongest point. As the course went on, the second half was more of a challenge. ")
improving_com.append("Throughout the course you continued to improve and finished the course strong. Keep up the hard work. ")
improving_com.append("You did well to improve throughout the course, the lastest part of the course was your strongest point. Your hard work is paying off. ")

ie_conc = []
ie_conc.append([" has not yet demostrated their skill in"," have not yet demostrated your skill in"])
ie_conc.append([" is in the initial stage of understanding their skill of"," are in the initial stage of understanding your skill of"])
ie_conc.append([" is highly encouraged to seek extra help for"," are highly encouraged to seej extra help for"])


emg_conc = []
emg_conc.append([" would benefit by spending more time practicing"," would benefit by spending more time practicing"])
emg_conc.append([" is encouraged to seek extra practice with"," are encouraged to seek extra practice with"])
emg_conc.append([" has not yet demonstrated the necessary skill in"," have not yet demonstrated the necessary skill in"])


dev_conc = []
dev_conc.append([" is encouraged to seek extra practice with"," are encouraged to seek extra practice with"])
dev_conc.append([" at times demonstrates the necessary skill in"," occasionally demonstrate the necessary skill in"])
dev_conc.append([" has partially met the expected skill in"," have partially met the expected skill in"])

pro_conc = []
pro_conc.append([", you display a strong skill in"," display a strong skill in"])
pro_conc.append([" demonstrates competent skill in"," demonstrate competent skill in"])
pro_conc.append([" meets the expected skill in"," meet the expected skill in"])

ext_conc = []
ext_conc.append([", you display exceptional skill in"," display exceptional skill in"])
ext_conc.append([" is able to demonstrate to a high degree their skill in"," are able to demonstrate to a high degree your skill in"])
ext_conc.append([" exceeds the expected skill in"," exceed the expected skill in"])

connecting_conc = []
connecting_conc.append([", which puts them at a proficiency scale of",",  which puts you at a proficiency scale of"])
connecting_conc.append([", on the proficiency scale they are at"," on the proficiency scale you are at"])
connecting_conc.append([" while having a proficiency scale of"," while having a proficiency scale of"])

def content_com(grade, name, content,x,bw,prof):
    ext = prof[0]
    pro = prof[1]
    dev = prof[2]
    emg = prof[3]
    name = name.split()[0]
    
    r = randrange(2)
    rr = randrange(2)
    
    if bw > 0:
        ad_com = '. This is your strongest part of the course. '
    elif bw < 0:
        ad_com = '. This is the part of the course you need to improve the most on. '
    else:
        ad_com = '. '
    if x == 0:
        if grade >= ext:
            comment = f"{name}{ext_cont[r][0]} {content} {connecting[rr][0]} extending{ad_com}"

        
        elif grade >= pro:
            r = randrange(4)
            rr = randrange(2)
            comment = f"{name}{pro_cont[r][0]} {content} {connecting[rr][0]} proficient{ad_com}"
        
            
        elif grade >= dev:
            comment = f"{name}{dev_cont[r][0]} {content} {connecting[rr][0]} developing{ad_com}"
        
        elif grade >= emg:
            r = randrange(3)
            rr = randrange(2)
            comment = f"{name}{emerging_cont[r][0]} {content} {connecting[rr][0]} emerging{ad_com}"
        else:
            r = randrange(2)
            rr = randrange(2)
            comment = f"{name}{ie_cont[r][0]} {content} {connecting[rr][0]} insufficient evidence{ad_com}"

    else:
        if grade >= ext:
            comment = f"You{ext_cont[r][1]} {content} {connecting[rr][1]} extending{ad_com}"
        
        elif grade >= pro:
            r = randrange(4)
            rr = randrange(2)
            comment = f"You{pro_cont[r][1]} {content} {connecting[rr][1]} proficient{ad_com}"
        
        
        elif grade >= dev:
            comment = f"You{dev_cont[r][1]} {content} {connecting[rr][1]} developing{ad_com}"
        
        elif grade >= emg:
            r = randrange(3)
            rr = randrange(2)
            comment = f"You{emerging_cont[r][1]} {content} {connecting[rr][1]} emerging{ad_com}"
        else:
            r = randrange(2)
            rr = randrange(2)
            comment = f"You{ie_cont[r][1]} {content} {connecting[rr][1]} insufficient evidence{ad_com}"
            
    return comment

def concept_com(grade, name, concept,x,bw,prof):
    ext = prof[0]
    pro = prof[1]
    dev = prof[2]
    emg = prof[3]
    name = name.split()[0]
    r = randrange(2)
    rr = randrange(2)
    
    if bw > 0:
        ad_com = ', this is your strongest skill. '
    else:
        ad_com = '. '
    if x == 0:
        if grade >= ext:
            comment = f"{name}{ext_conc[r][0]} {concept}{connecting_conc[rr][0]} extending{ad_com}"
    
        elif grade >= pro:
            comment = f"{name}{pro_conc[r][0]} {concept}{connecting_conc[rr][0]} proficient{ad_com}"

        elif grade >= dev:
            comment = f"{name}{dev_conc[r][0]} {concept}{connecting_conc[rr][0]} developing{ad_com}"

        elif grade >= emg:
            comment = f"{name}{emg_conc[r][0]} {concept} {connecting_conc[rr][0]} emerging{ad_com}"
        else:
            comment = f"{name}{ie_conc[r][0]} {concept} {connecting_conc[rr][0]} insufficient evidence{ad_com}"
                
    else:
        if grade >= ext:
            comment = f"You{ext_conc[r][1]} {concept}{connecting_conc[rr][1]} extending{ad_com}"
        
        elif grade >= pro:
            comment = f"You{pro_conc[r][1]} {concept}{connecting_conc[rr][1]} proficient{ad_com}"
        
        elif grade >= dev:
            comment = f"You{dev_conc[r][1]} {concept}{connecting_conc[rr][1]} developing{ad_com}"
        
        elif grade >= emg:
            comment = f"You{emg_conc[r][1]} {concept} {connecting_conc[rr][1]} emerging{ad_com}"
        else:
            comment = f"You{ie_conc[r][1]} {concept} {connecting_conc[rr][1]} insufficient evidence{ad_com}"

    return comment

def overall_com(grade, name, course_name, prof, consistent,improving):
    ext = prof[0]
    pro = prof[1]
    dev = prof[2]
    emg = prof[3]
    name = name.split()[0]
    if grade >= ext:
        proficiency = 'be extending'
    
    elif grade >= pro:
        proficiency = 'be proficient'
        
        
    elif grade >= dev:
        proficiency = 'be developing'
         
    elif grade >= emg:
        proficiency = 'be emerging'
    else:
        proficiency = 'have insufficient evidence'


    comment = f"{name}, overall in the course you have shown to {proficiency} in {course_name}. \n"
    if consistent > 0.9:
        comment += f"Throughout the course you did well to consistently hand in your best work. "
    elif consistent < 0.85 and consistent > 0:
        comment += f"Throughout the course you did not take the opportunity to consistently hand in your best work. "

    r = randrange(2)
    if improving == 0:
        mm = 0
    elif sum(improving[0:int(len(improving)/2)])>1:
        comment += improving_com[r]
    elif sum(improving[int(len(improving)/2):-1])>1:
        comment += improving_com[r+2]

    return comment















