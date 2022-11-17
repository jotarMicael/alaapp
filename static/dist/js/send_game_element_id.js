function send_game_element_id(game_element_id,type) {
  
    if (type=='#send_challenge' || type=='#change_state_challenge'){
      $("#challenge_id").val(game_element_id);
      
    }
    else{
      $("#badge_id").val(game_element_id);
    }
    $.confirmation(type);
      
  }
