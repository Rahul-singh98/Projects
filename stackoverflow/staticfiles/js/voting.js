$('img.upvote').click(function () {
        console.log("image upvoting")
        var id = '{{ question.id }}';
        var vote_type = 'up';

        if ($(this).hasClass('selected')) {
            var vote_action = 'recall-vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                console.log("upvote recall")
                if (Number.isInteger(response)) {
                    $('img.upvote').removeAttr('src')
                        .attr('src', '/static/images/upvote-off.svg')
                        .removeClass('selected');
                }
            });
        } else {
            var vote_action = 'vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                console.log("upvoted")
                if (Number.isInteger(response)) {
                    $('img.upvote').removeAttr('src')
                        .attr('src', '/static/images/upvote-on.svg')
                        .addClass('selected')
                }
            });
        }
    })

    $('img.downvote').click(function () {
        console.log("image downvoting")
        var id = '{{ question.id }}';
        var vote_type = 'up';

        if ($(this).hasClass('selected')) {
            var vote_action = 'recall-vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                console.log("downvoted recall")
                if (Number.isInteger(response)) {
                    $('img.downvote').removeAttr('src')
                        .attr('src', '/static/images/downvote-off.svg')
                        .removeClass('selected');
                }
            });
        } else {
            var vote_action = 'vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                console.log("downvote")
                if (Number.isInteger(response)) {
                    $('img.downvote').removeAttr('src')
                        .attr('src', '/static/images/downvote-on.svg')
                        .addClass('selected')
                }
            });
        }
    })