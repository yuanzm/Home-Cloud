$myName = $('#my-name')
$likeIcon = $('.like-icon')

requestChangeLike = (myName, dataId, dataType, likeChange)->
	url = '/data/changelike'
	data =
		myName: myName
		dataId: dataId
		dataType: dataType
		likeChange: likeChange
	$.ajax({
		type: "POST"
		url: url
		data: data
		success: (data)->
			console.log data
	})

showLoginAlert = ->
	alert('请先登录')

class Like
	constructor:->
	bindHandler: ->
		$likeIcon.bind 'click', ->
			if $myName.text()
				$likeNum = $(@).parent().parent().parent()
							.siblings('.panel-heading')
							.find('.data-likes')
				currentText = $likeNum.text()
				console.log currentText
				dataType = $(@).data('datatype')
				id = $(@).data('id')
				$(@).toggleClass('liked')
				if $(@).hasClass('liked')
					requestChangeLike($myName.text(), id, dataType, 1)
					$likeNum.text(Number(currentText) + 1)
				else
					requestChangeLike($myName.text(), id, dataType, -1)
					$likeNum.text(Number(currentText) - 1)
			else
				showLoginAlert()

module.exports = Like

