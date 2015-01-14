$commentBtn = $('.comment-button')
$myName = $('#my-name')
$commentInput = $('#comment-input')
$window = $(window)
$allComment = $('#comments')


addComment = (myName, dataId, dataType, commentText, callback)->
	url = '/data/addcomment'
	data =
		myName: myName
		dataId: dataId
		dataType: dataType
		commentText: commentText

	$.ajax({
		type: "POST"
		url: url
		data: data
		success: ->
			callback()
	})

showLoginAlert = ->
	alert("请先登录")

getCurrentIndex =->
	return $allComment.find('li').length

appendComment = (commentText)->
	index = getCurrentIndex()
	comment = '<li>'
	comment += '<p>' 
	comment += '<span>#' + (index + 1) + '楼 </span>'
	comment += '<span>' + $myName.text() + '</span>'
	comment += '</p>'
	comment += '<p>' + '<span>' + commentText + '</span></p>'
	comment += '</li>'
	$allComment.append($(comment))

class Comment
	constructor:->
	bindHandler: ->
		self = @
		$commentBtn.bind 'click', self.sendComment
	sendComment: ->
		if $myName.text()
			dataType = $(@).data('datatype')
			id = $(@).data('id')
			commentText = $commentInput.val()
			if commentText isnt ''
				addComment $myName.text(), id, dataType, commentText, ->
					$commentInput.val(' ')
					appendComment(commentText)
		else
			showLoginAlert()

module.exports = Comment
