   
        $.ajax({
            url: /game_element_view/,
            type: 'POST',
            data: {
                'action': 'search_time_restriction_id',
                'id': $('#id_project').val()
            },
            dataType: 'json',
        }).done(function (data) {
            if (!data.hasOwnProperty('error')) {             
                viewInMap(data[2]);

            }
            else{
              
            }

        }).fail(function (jqXHR, textStatus, errorThrown) {
            viewInMap(null);
        })
    


