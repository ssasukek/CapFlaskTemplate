function getBotResponse(input){
    if (input == greetings.toLowerCase()){
        return "hello";
    }
    else{
        return "I don't undestand what you're saying :("
    }
}
greetings = ["hello", "hi", "hey", "sup", "greetings"]; 
greetings.some(); 