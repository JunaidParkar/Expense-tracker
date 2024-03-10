"use strict";

function _typeof(o) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (o) { return typeof o; } : function (o) { return o && "function" == typeof Symbol && o.constructor === Symbol && o !== Symbol.prototype ? "symbol" : typeof o; }, _typeof(o); }
function _createForOfIteratorHelper(o, allowArrayLike) { var it = typeof Symbol !== "undefined" && o[Symbol.iterator] || o["@@iterator"]; if (!it) { if (Array.isArray(o) || (it = _unsupportedIterableToArray(o)) || allowArrayLike && o && typeof o.length === "number") { if (it) o = it; var i = 0; var F = function F() {}; return { s: F, n: function n() { if (i >= o.length) return { done: true }; return { done: false, value: o[i++] }; }, e: function e(_e) { throw _e; }, f: F }; } throw new TypeError("Invalid attempt to iterate non-iterable instance.\nIn order to be iterable, non-array objects must have a [Symbol.iterator]() method."); } var normalCompletion = true, didErr = false, err; return { s: function s() { it = it.call(o); }, n: function n() { var step = it.next(); normalCompletion = step.done; return step; }, e: function e(_e2) { didErr = true; err = _e2; }, f: function f() { try { if (!normalCompletion && it["return"] != null) it["return"](); } finally { if (didErr) throw err; } } }; }
function _unsupportedIterableToArray(o, minLen) { if (!o) return; if (typeof o === "string") return _arrayLikeToArray(o, minLen); var n = Object.prototype.toString.call(o).slice(8, -1); if (n === "Object" && o.constructor) n = o.constructor.name; if (n === "Map" || n === "Set") return Array.from(o); if (n === "Arguments" || /^(?:Ui|I)nt(?:8|16|32)(?:Clamped)?Array$/.test(n)) return _arrayLikeToArray(o, minLen); }
function _arrayLikeToArray(arr, len) { if (len == null || len > arr.length) len = arr.length; for (var i = 0, arr2 = new Array(len); i < len; i++) arr2[i] = arr[i]; return arr2; }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(t) { var i = _toPrimitive(t, "string"); return "symbol" == _typeof(i) ? i : String(i); }
function _toPrimitive(t, r) { if ("object" != _typeof(t) || !t) return t; var e = t[Symbol.toPrimitive]; if (void 0 !== e) { var i = e.call(t, r || "default"); if ("object" != _typeof(i)) return i; throw new TypeError("@@toPrimitive must return a primitive value."); } return ("string" === r ? String : Number)(t); }
var FormValidator = /*#__PURE__*/function () {
  function FormValidator(form) {
    var isRequiredAll = arguments.length > 1 && arguments[1] !== undefined ? arguments[1] : false;
    var requiredNone = arguments.length > 2 && arguments[2] !== undefined ? arguments[2] : [];
    var option = arguments.length > 3 && arguments[3] !== undefined ? arguments[3] : [{
      type: "checkbox",
      allowed_from: [{
        el: [],
        number_of_allowed: 0
      }]
    }, {
      type: "custom_required",
      func: null
    }];
    _classCallCheck(this, FormValidator);
    this.form = form;
    this.isRequiredAll = isRequiredAll;
    this.isRequiredNone = requiredNone;
    this.options = option;
    this.toSetRequired = ["date", "datetime-local", "email", "file", "image", "number", "password", "tel", "text", "time", "url", "week", "hidden"];
  }
  _createClass(FormValidator, [{
    key: "setRequired",
    value: function setRequired() {
      var _this = this;
      Array.from(this.form.getElementsByTagName("input")).forEach(function (tag) {
        if (_this.toSetRequired.includes(tag.type) && _this.isRequiredAll) {
          var cr = false;
          var _iterator = _createForOfIteratorHelper(_this.options),
            _step;
          try {
            for (_iterator.s(); !(_step = _iterator.n()).done;) {
              var elem = _step.value;
              if (elem.type == "custom_required" && elem.func != null) {
                tag.setAttribute("isRequired", true);
                cr = true;
                break;
              }
              if (elem.type == "custom_required" && elem.func == null) {
                cr = false;
                break;
              }
            }
          } catch (err) {
            _iterator.e(err);
          } finally {
            _iterator.f();
          }
          if (!cr) {
            tag.required = true;
          }
        }
      });
    }
  }, {
    key: "verifyRequirement",
    value: function verifyRequirement(obj) {
      if (obj.type == "checkbox") {
        obj.allowed_from.forEach(function (al) {
          if (al.number_of_allowed > al.el.length || al.number_of_allowed < 0) {
            console.error("Counting error: In options elements list should be greater than number of allowed elements");
          } else {
            var clicked = [];
            al.el.forEach(function (element) {
              element.onclick = function () {
                if (element.checked) {
                  clicked.push(element);
                  if (clicked.length > al.number_of_allowed) {
                    clicked.shift();
                  }
                  al.el.forEach(function (element2) {
                    if (clicked.includes(element2)) {
                      element2.checked = true;
                    } else {
                      element2.checked = false;
                    }
                  });
                } else {
                  element.checked = false;
                  var newClicked = clicked.filter(function (item) {
                    return item !== element;
                  });
                  clicked = newClicked;
                }
              };
            });
          }
        });
      }
    }
  }, {
    key: "submitter",
    value: function submitter(e, success) {
      e.preventDefault();
      var err = false;
      var _iterator2 = _createForOfIteratorHelper(this.options),
        _step2;
      try {
        for (_iterator2.s(); !(_step2 = _iterator2.n()).done;) {
          var opt = _step2.value;
          if (opt.type == "custom_required" && opt.func != null) {
            var inputs = Array.from(this.form.querySelectorAll("[isRequired]"));
            for (var _i = 0, _inputs = inputs; _i < _inputs.length; _i++) {
              var inp = _inputs[_i];
              if (inp.value.trim() == "") {
                opt.func("Please proide value for ".concat(inp.name));
                err = true;
                break;
              }
            }
            break;
          }
          if (opt.type == "checkbox") {
            var _iterator3 = _createForOfIteratorHelper(opt.allowed_from),
              _step3;
            try {
              for (_iterator3.s(); !(_step3 = _iterator3.n()).done;) {
                var allowed = _step3.value;
                if (allowed.el.length > 0) {
                  var count = 0;
                  var _iterator4 = _createForOfIteratorHelper(allowed.el),
                    _step4;
                  try {
                    for (_iterator4.s(); !(_step4 = _iterator4.n()).done;) {
                      var el = _step4.value;
                      if (el.checked) {
                        count++;
                      }
                    }
                  } catch (err) {
                    _iterator4.e(err);
                  } finally {
                    _iterator4.f();
                  }
                  if (count != allowed.number_of_allowed) {
                    err = true;
                    var isCustom = false;
                    var _iterator5 = _createForOfIteratorHelper(this.options),
                      _step5;
                    try {
                      for (_iterator5.s(); !(_step5 = _iterator5.n()).done;) {
                        var ell = _step5.value;
                        if (ell.type == "custom_required" && ell.func != null) {
                          isCustom = true;
                          ell.func("Chcekboxes not selected");
                          break;
                        }
                      }
                    } catch (err) {
                      _iterator5.e(err);
                    } finally {
                      _iterator5.f();
                    }
                    isCustom ? "" : console.error("Form error: Check box not selected");
                    break;
                  }
                }
              }
            } catch (err) {
              _iterator3.e(err);
            } finally {
              _iterator3.f();
            }
          }
        }
      } catch (err) {
        _iterator2.e(err);
      } finally {
        _iterator2.f();
      }
      if (!err) {
        success();
      }
    }
  }, {
    key: "validate",
    value: function validate(success) {
      var _this2 = this;
      this.setRequired();
      this.options.forEach(function (obj) {
        _this2.verifyRequirement(obj);
      });
      this.form.addEventListener("submit", function (e) {
        _this2.submitter(e, success);
      });
    }
  }, {
    key: "revert",
    value: function revert() {
      var _this3 = this;
      if (!this.form) return;
      Array.from(this.form.querySelectorAll("[isRequired]")).forEach(function (tag) {
        tag.removeAttribute("isRequired");
      });
      if (this.isRequiredAll) {
        Array.from(this.form.querySelectorAll("[data-required]")).forEach(function (tag) {
          tag.required = false;
          tag.removeAttribute("data-required");
        });
      }
      this.form.removeEventListener("submit", function (e) {
        _this3.submitter(e);
      });
    }
  }]);
  return FormValidator;
}();