function getBotResponse(input){
    if (input == "hello" || input == "hi" || input == "hey" || input == "sup" || input == "greetings"){
        return "hello";
    }
    if(input == "options"){
        return "here's links to our climate page : https://127.0.0.1:5000/climatechange . A link to our about-us page : https://127.0.0.1:5000/aboutus . ";
    }
    else{
        return "I don't undestand what you're saying :("; 
    }
}