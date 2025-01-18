index_mappings = {
    "properties":{
        "original_title":{
            "type" : "text"
        },
        "overview":{
            "type" : "text"
        },
        "vote_average":{
            "type" : "float"
        },
        "vote_count":{
            "type" : "long"
        },
        "overview_vector":{
            "type" : "dense_vector",
            "dims" : 768,
            "index" : True,
            "similarity" : "l2_norm"
        }
    }
}