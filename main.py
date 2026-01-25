from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field, feild_validator
from typing import Literal, Annotated
import pickle
import pandas as pd

# step 1 import the ml model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)
   
app = FastAPI()

# list of the cities and their tiers:
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

# step 2: creating pydantic model to validate coming data

class UserInput(BaseModel):
    age: Annotated[int,  Field(..., gt=0, lt=120, description="Age of the user in years")]
    weight: Annotated[float, Field(..., gt=0, description="Weight of the user in kgs")]
    height: Annotated[float, Field(..., gt=0, ly=2.5, description="Height of the user in cms")]
    income_lpa: Annotated[float, Field(..., gt=0, description="Income of the user in lakhs per annum")]
    smoker: Annotated[bool, Field(..., description="Whether the user is a smoker or not")]
    city: Annotated[str, Field(..., description="City where the user resides")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]
    # we will create a feild validator city
    @feild_validator
    @classmethod
    def city_validate(cls, value: str):
        value = value.strip().title()
        return value
    
    # now with these we have to make new features :
    #computed feild 1: bmi--------------------------------
    @computed_field
    @property
    def BMI(self)->float:
        return self.weight/(self.height**2)
    
    # computed field 2: lifestyle risk------------------------------
    @computed_field
    @property
    def lifetyle_risk(self)->str:
        if self.smoker and self.BMI >30:
            return "high"
        elif self.smoker or self.BMI >27:
            return "medium"
        else:
            return "low"
        
    # computed filed 3: age group------------------------------ 
    @computed_field
    @property
    def age_group(self)->str:
        if self.age <25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age<60:
            return "middle_aged"
        return "senior"
    
    # computed field 4: city tier--------------------------------
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2 
        else:
            return 3  
# Home endpoint
@app.get("/")
def hello():
    return {"message":"Welcome to Insurance premium prediction API"} 
# creating the route which we want that is /predict
@app.post("/predict")
def predict_premium(data: UserInput):
    # we will first create the dataframe since our model which is randomforest has been trained on dataframe
    
    input_df = pd.DataFrame([{
        'BMI': data.BMI,
        'age_group': data.age_group,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation,
        'lifestyle_risk': data.lifetyle_risk        
    }])
    # now we have to predict for that we will call our prediction model
    prediction = model.predict(input_df)[0]
    
    return JSONResponse(status_code=200, content={"predicted_category": prediction})
    
    
