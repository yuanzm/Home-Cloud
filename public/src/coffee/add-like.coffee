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
	constructor: (@page)->
	init: ->
		console.log @page
		if @page is 'data-list'
			@bindHandler()
		else
			@detailPageBind()
	bindHandler: ->
		$likeIcon.bind 'click', ->
			if $myName.text()
				# $(@).toggleClass('liked')
				$likeNum = $(@).parent().parent().parent()
							.siblings('.panel-heading')
							.find('.data-likes')
				currentText = $likeNum.text()
				dataType = $(@).data('datatype')
				id = $(@).data('id')
				if $(@).hasClass('liked')
					$(@).addClass('liked')
					requestChangeLike($myName.text(), id, dataType, 1)
					$likeNum.text(Number(currentText) + 1)
				else
					$(@).removeClass('liked')
					requestChangeLike($myName.text(), id, dataType, -1)
					$likeNum.text(Number(currentText) - 1)
			else
				showLoginAlert()
	detailPageBind: ->
		$likeIcon.bind 'click', ->
			if $myName.text()
				dataType = $(@).data('datatype')
				id = $(@).data('id')
				$(@).toggleClass('liked')
				if $(@).hasClass('liked')
					requestChangeLike($myName.text(), id, dataType, 1)
				else
					requestChangeLike($myName.text(), id, dataType, -1)
module.exports = Like

