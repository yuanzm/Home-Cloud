(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
var $likeButton, $likeIcon, $likes, $myName, Like, requestChangeLike, showLoginAlert;

$myName = $('#my-name');

$likeIcon = $('.like-icon');

$likeButton = $('.detail-like-button');

$likes = $('#likes');


/*
 * @param {String} myName: A String indicating the name of user who click the `like` button
 * @param {String} dataId: A String indicating the id of the picture or video
 * @param {String} dataType: A String indicating type of the data
 * @param {Number} likeChange: A number indicating `add` like or `remove` like
 */

requestChangeLike = function(myName, dataId, dataType, likeChange) {
  var data, url;
  url = '/data/changelike';
  data = {
    myName: myName,
    dataId: dataId,
    dataType: dataType,
    likeChange: likeChange
  };
  return $.ajax({
    type: "POST",
    url: url,
    data: data,
    success: function(data) {}
  });
};


/*
 * show `login` alert
 */

showLoginAlert = function() {
  return alert('请先登录');
};


/*
 * A class for adding a like to a picture or a video
 */

Like = (function() {

  /*
  	 * init the Like
   */
  function Like(page) {
    this.page = page;
  }


  /*
  	 * Bind event handler for the `like-button` in different pages according to `page` value
   */

  Like.prototype.init = function() {
    if (this.page === 'data-list') {
      return this.bindHandler();
    } else {
      return this.detailPageBind();
    }
  };


  /*
  	 * Event handler for `data-list` page
   */

  Like.prototype.bindHandler = function() {
    return $likeIcon.bind('click', function() {
      var $likeNum, currentText, dataType, id;
      if ($myName.text()) {
        $likeNum = $(this).parent().parent().parent().siblings('.panel-heading').find('.data-likes');
        currentText = $likeNum.text();
        dataType = $(this).data('datatype');
        id = $(this).data('id');
        if ($(this).hasClass('liked')) {
          $(this).removeClass('liked');
          requestChangeLike($myName.text(), id, dataType, -1);
          return $likeNum.text(Number(currentText) - 1);
        } else {
          $(this).addClass('liked');
          requestChangeLike($myName.text(), id, dataType, 1);
          return $likeNum.text(Number(currentText) + 1);
        }
      } else {
        return showLoginAlert();
      }
    });
  };


  /*
  	* Event handler for `data-detail` page
   */

  Like.prototype.detailPageBind = function() {
    return $likeButton.bind('click', function() {
      var currentIndex, dataType, id;
      if ($myName.text()) {
        dataType = $(this).data('datatype');
        id = $(this).data('id');
        currentIndex = $likes.text();
        if ($(this).hasClass('liked')) {
          $(this).removeClass('liked').find('p').text('点赞 +1');
          $likes.text('赞 ' + (Number(currentIndex.slice(2, currentIndex.length)) - 1));
          return requestChangeLike($myName.text(), id, dataType, -1);
        } else {
          $(this).addClass('liked').find('p').text('已点赞');
          $likes.text('赞 ' + (Number(currentIndex.slice(2, currentIndex.length)) + 1));
          return requestChangeLike($myName.text(), id, dataType, 1);
        }
      } else {
        return showLoginAlert();
      }
    });
  };

  return Like;

})();

module.exports = Like;



},{}],2:[function(require,module,exports){
var $allComment, $commentBtn, $commentInput, $myName, $window, Comment, addComment, appendComment, getCurrentIndex, showLoginAlert;

$commentBtn = $('.comment-button');

$myName = $('#my-name');

$commentInput = $('#comment-input');

$window = $(window);

$allComment = $('#comments');

addComment = function(myName, dataId, dataType, commentText, callback) {
  var data, url;
  url = '/data/addcomment';
  data = {
    myName: myName,
    dataId: dataId,
    dataType: dataType,
    commentText: commentText
  };
  return $.ajax({
    type: "POST",
    url: url,
    data: data,
    success: function() {
      return callback();
    }
  });
};

showLoginAlert = function() {
  return alert("请先登录");
};

getCurrentIndex = function() {
  return $allComment.find('li').length;
};

appendComment = function(commentText) {
  var comment, index;
  index = getCurrentIndex();
  comment = '<li>';
  comment += '<p>';
  comment += '<span>#' + (index + 1) + '楼 </span>';
  comment += '<span>' + $myName.text() + '</span>';
  comment += '</p>';
  comment += '<p>' + '<span>' + commentText + '</span></p>';
  comment += '</li>';
  return $allComment.append($(comment));
};

Comment = (function() {
  function Comment() {}

  Comment.prototype.bindHandler = function() {
    var self;
    self = this;
    return $commentBtn.bind('click', self.sendComment);
  };

  Comment.prototype.sendComment = function() {
    var commentText, dataType, id;
    if ($myName.text()) {
      dataType = $(this).data('datatype');
      id = $(this).data('id');
      commentText = $commentInput.val();
      if (commentText !== '') {
        return addComment($myName.text(), id, dataType, commentText, function() {
          $commentInput.val(' ');
          return appendComment(commentText);
        });
      }
    } else {
      return showLoginAlert();
    }
  };

  return Comment;

})();

module.exports = Comment;



},{}],3:[function(require,module,exports){
var Comment, Like, comment, like, like2;

Like = require("./add-like.coffee");

Comment = require("./comment.coffee");

like = new Like('data-list');

like.init();

like2 = new Like('data-detail');

like2.init();

comment = new Comment();

comment.bindHandler();



},{"./add-like.coffee":1,"./comment.coffee":2}]},{},[3]);
