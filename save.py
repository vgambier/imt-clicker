# File format :
# a dictionary with keys = "ects", "achievements", "signature"
# achievements = a list of bools

import hmac
import json
import achievements

SAVE_FILE_PATH="save.imt"

class Save :

    def save(ects,achievement_list=achievements.achievement_list):
        save_file=open(SAVE_FILE_PATH,'w')
        json.dump(Save.to_save_format(ects, achievement_list), save_file)
        save_file.close()

    # return [ects, achievement_list, signature_is_correct]
    def load(achievement_list=achievements.achievement_list):
        new_achievement_list=achievement_list.copy()
        save_file=open(SAVE_FILE_PATH,'r')
        data= json.load(save_file)
        save_file.close()
        ects=data["ects"]
        new_achievement_list=data["achievements"]
        signature_is_correct = Save.verify_signature(data)
        return [ects, new_achievement_list, signature_is_correct]
    
    def to_save_format(ects, achievement_list=achievements.achievement_list):
        data=dict()
        data["ects"]=ects
        data["achievements"]=achievement_list
        data["signature"]=Save.signature(data)
        return data
    
    # return a bool
    # delete the signature from data
    def verify_signature(data):
        signature=data.pop("signature")
        return signature == Save.signature(data)
    
    # return a string
    def signature(data):
        string=json.dumps(data)
        not_secret_key=b"For real, this is not the secret key. Look away please UwU."
        hashed=hmac.new(not_secret_key)
        hashed.update(bytes(string,'utf-8'))
        hashed=str(hashed.digest())
        hashed=hashed.replace("'","")
        hashed=hashed.replace("\\x","")
        return hashed[1:]

