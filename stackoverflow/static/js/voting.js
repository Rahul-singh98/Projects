$('img.upvote').click(function () {
        var id = '{{ question.id }}';
        var vote_type = 'up';

        if ($(this).hasClass('selected')) {
            var vote_action = 'recall-vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                if (Number.isInteger(response)) {
                    $('img.upvote').removeAttr('src')
                        .attr('src', '/static/images/upvote-off.svg')
                        .removeClass('selected');
                }
            });
        } else {
            var vote_action = 'vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                if (Number.isInteger(response)) {
                    $('img.upvote').removeAttr('src')
                        .attr('src', '/static/images/upvote-on.svg')
                        .addClass('selected')
                }
            });
        }
    })

    $('img.downvote').click(function () {
        var id = '{{ question.id }}';
        var vote_type = 'up';

        if ($(this).hasClass('selected')) {
            var vote_action = 'recall-vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                if (Number.isInteger(response)) {
                    $('img.downvote').removeAttr('src')
                        .attr('src', '/static/images/downvote-off.svg')
                        .removeClass('selected');
                }
            });
        } else {
            var vote_action = 'vote'
            $.post('/question/vote', { id: id, type: vote_type, action: vote_action, csrfmiddlewaretoken: '{{ csrf_token }}' }, function (response) {
                if (Number.isInteger(response)) {
                    $('img.downvote').removeAttr('src')
                        .attr('src', '/static/images/downvote-on.svg')
                        .addClass('selected')
                }
            });
        }
    })