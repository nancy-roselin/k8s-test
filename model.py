import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def tour(t_n,s):
    string="Tourism_DataSet_"+t_n+".csv"
    df=pd.read_csv(string)
    if s=="top_p":
        top_Val=4
    elif s=="all_p":
        tour_place=list(df.Place.unique())
        total=len(tour_place)
        top_Val=total
    else:
        df = df[["Place", "Rating"]]
        df = df.groupby(['Place']).agg({'Rating':[np.mean]})
        data_dict = df.to_dict()
        print(data_dict)
        #new_list = list(data_dict.items())
        #print(new_list)
        return data_dict
    def get_Place_from_index(index):
        return df[df.index == index]["Place"].values[0]
    
    def get_index_from_Place(Place):
        return df[df.Place == Place]["index"].values[0]
    def combine_features(row):
        return (str(row['Rating'])+" "+str(row['Setiment_Value']))    
    ##############################################
    df = df.assign(index = [x for x in range(0,len(df))])
    #features on which I'm going to perform cosine similarity
    features = ['Rating','Setiment_Value']
    for feature in features:
        df[feature] = df[feature].fillna('') #filling all NaNs with blank string
    df["combined_features"] = df.apply(combine_features,axis=1) #applying combined_features() method over each rows of dataframe and storing the combined string in "combined_features" column
    df.iloc[0].combined_features
    #df = df.iloc[:200000]
    df=df.head(20000)
    cv = CountVectorizer() #creating new CountVectorizer() object
    count_matrix = cv.fit_transform(df["combined_features"]) #feeding combined strings(contents) to CountVectorizer() object
    cosine_sim = cosine_similarity(count_matrix)
    sample=df["Place"]
    sample_place=sample[0]
    place_index = get_index_from_Place(sample_place)
    recommendation_place =  list(enumerate(cosine_sim[place_index]))
        #sorting in descending order
    sorted_recommendation_place = sorted(recommendation_place,key=lambda x:x[1],reverse=True)
    i=0
    
    list1=[]
    for element in sorted_recommendation_place:
        #print (get_Place_from_index(element[0]))
        #l.append(get_Place_from_index(element[0]))
        place=get_Place_from_index(element[0])
        if place not in list1:
            list1.append(place)
            i=i+1
        if i>top_Val:
            break
    print(list1)
    return list1
    

    
