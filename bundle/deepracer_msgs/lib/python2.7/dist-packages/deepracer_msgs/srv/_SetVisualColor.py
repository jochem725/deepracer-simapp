# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from deepracer_msgs/SetVisualColorRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import std_msgs.msg

class SetVisualColorRequest(genpy.Message):
  _md5sum = "c993776acc4e7a226360c9194290bf99"
  _type = "deepracer_msgs/SetVisualColorRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """string link_name
string visual_name
std_msgs/ColorRGBA ambient
std_msgs/ColorRGBA diffuse
std_msgs/ColorRGBA specular
std_msgs/ColorRGBA emissive
bool block

================================================================================
MSG: std_msgs/ColorRGBA
float32 r
float32 g
float32 b
float32 a
"""
  __slots__ = ['link_name','visual_name','ambient','diffuse','specular','emissive','block']
  _slot_types = ['string','string','std_msgs/ColorRGBA','std_msgs/ColorRGBA','std_msgs/ColorRGBA','std_msgs/ColorRGBA','bool']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       link_name,visual_name,ambient,diffuse,specular,emissive,block

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetVisualColorRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.link_name is None:
        self.link_name = ''
      if self.visual_name is None:
        self.visual_name = ''
      if self.ambient is None:
        self.ambient = std_msgs.msg.ColorRGBA()
      if self.diffuse is None:
        self.diffuse = std_msgs.msg.ColorRGBA()
      if self.specular is None:
        self.specular = std_msgs.msg.ColorRGBA()
      if self.emissive is None:
        self.emissive = std_msgs.msg.ColorRGBA()
      if self.block is None:
        self.block = False
    else:
      self.link_name = ''
      self.visual_name = ''
      self.ambient = std_msgs.msg.ColorRGBA()
      self.diffuse = std_msgs.msg.ColorRGBA()
      self.specular = std_msgs.msg.ColorRGBA()
      self.emissive = std_msgs.msg.ColorRGBA()
      self.block = False

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.link_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.visual_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_16fB().pack(_x.ambient.r, _x.ambient.g, _x.ambient.b, _x.ambient.a, _x.diffuse.r, _x.diffuse.g, _x.diffuse.b, _x.diffuse.a, _x.specular.r, _x.specular.g, _x.specular.b, _x.specular.a, _x.emissive.r, _x.emissive.g, _x.emissive.b, _x.emissive.a, _x.block))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.ambient is None:
        self.ambient = std_msgs.msg.ColorRGBA()
      if self.diffuse is None:
        self.diffuse = std_msgs.msg.ColorRGBA()
      if self.specular is None:
        self.specular = std_msgs.msg.ColorRGBA()
      if self.emissive is None:
        self.emissive = std_msgs.msg.ColorRGBA()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.link_name = str[start:end].decode('utf-8')
      else:
        self.link_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.visual_name = str[start:end].decode('utf-8')
      else:
        self.visual_name = str[start:end]
      _x = self
      start = end
      end += 65
      (_x.ambient.r, _x.ambient.g, _x.ambient.b, _x.ambient.a, _x.diffuse.r, _x.diffuse.g, _x.diffuse.b, _x.diffuse.a, _x.specular.r, _x.specular.g, _x.specular.b, _x.specular.a, _x.emissive.r, _x.emissive.g, _x.emissive.b, _x.emissive.a, _x.block,) = _get_struct_16fB().unpack(str[start:end])
      self.block = bool(self.block)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.link_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self.visual_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      _x = self
      buff.write(_get_struct_16fB().pack(_x.ambient.r, _x.ambient.g, _x.ambient.b, _x.ambient.a, _x.diffuse.r, _x.diffuse.g, _x.diffuse.b, _x.diffuse.a, _x.specular.r, _x.specular.g, _x.specular.b, _x.specular.a, _x.emissive.r, _x.emissive.g, _x.emissive.b, _x.emissive.a, _x.block))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.ambient is None:
        self.ambient = std_msgs.msg.ColorRGBA()
      if self.diffuse is None:
        self.diffuse = std_msgs.msg.ColorRGBA()
      if self.specular is None:
        self.specular = std_msgs.msg.ColorRGBA()
      if self.emissive is None:
        self.emissive = std_msgs.msg.ColorRGBA()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.link_name = str[start:end].decode('utf-8')
      else:
        self.link_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.visual_name = str[start:end].decode('utf-8')
      else:
        self.visual_name = str[start:end]
      _x = self
      start = end
      end += 65
      (_x.ambient.r, _x.ambient.g, _x.ambient.b, _x.ambient.a, _x.diffuse.r, _x.diffuse.g, _x.diffuse.b, _x.diffuse.a, _x.specular.r, _x.specular.g, _x.specular.b, _x.specular.a, _x.emissive.r, _x.emissive.g, _x.emissive.b, _x.emissive.a, _x.block,) = _get_struct_16fB().unpack(str[start:end])
      self.block = bool(self.block)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_16fB = None
def _get_struct_16fB():
    global _struct_16fB
    if _struct_16fB is None:
        _struct_16fB = struct.Struct("<16fB")
    return _struct_16fB
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from deepracer_msgs/SetVisualColorResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetVisualColorResponse(genpy.Message):
  _md5sum = "2ec6f3eff0161f4257b808b12bc830c2"
  _type = "deepracer_msgs/SetVisualColorResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """bool success
string status_message
"""
  __slots__ = ['success','status_message']
  _slot_types = ['bool','string']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       success,status_message

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetVisualColorResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.success is None:
        self.success = False
      if self.status_message is None:
        self.status_message = ''
    else:
      self.success = False
      self.status_message = ''

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(_get_struct_B().pack(self.success))
      _x = self.status_message
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      start = end
      end += 1
      (self.success,) = _get_struct_B().unpack(str[start:end])
      self.success = bool(self.success)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.status_message = str[start:end].decode('utf-8')
      else:
        self.status_message = str[start:end]
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
class SetVisualColor(object):
  _type          = 'deepracer_msgs/SetVisualColor'
  _md5sum = '9c987659e93e8e993b90a6ea6fab5b74'
  _request_class  = SetVisualColorRequest
  _response_class = SetVisualColorResponse
