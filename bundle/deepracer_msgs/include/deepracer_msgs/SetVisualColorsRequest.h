// Generated by gencpp from file deepracer_msgs/SetVisualColorsRequest.msg
// DO NOT EDIT!


#ifndef DEEPRACER_MSGS_MESSAGE_SETVISUALCOLORSREQUEST_H
#define DEEPRACER_MSGS_MESSAGE_SETVISUALCOLORSREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/ColorRGBA.h>
#include <std_msgs/ColorRGBA.h>
#include <std_msgs/ColorRGBA.h>
#include <std_msgs/ColorRGBA.h>

namespace deepracer_msgs
{
template <class ContainerAllocator>
struct SetVisualColorsRequest_
{
  typedef SetVisualColorsRequest_<ContainerAllocator> Type;

  SetVisualColorsRequest_()
    : link_names()
    , visual_names()
    , ambients()
    , diffuses()
    , speculars()
    , emissives()
    , block(false)  {
    }
  SetVisualColorsRequest_(const ContainerAllocator& _alloc)
    : link_names(_alloc)
    , visual_names(_alloc)
    , ambients(_alloc)
    , diffuses(_alloc)
    , speculars(_alloc)
    , emissives(_alloc)
    , block(false)  {
  (void)_alloc;
    }



   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _link_names_type;
  _link_names_type link_names;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _visual_names_type;
  _visual_names_type visual_names;

   typedef std::vector< ::std_msgs::ColorRGBA_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::std_msgs::ColorRGBA_<ContainerAllocator> >::other >  _ambients_type;
  _ambients_type ambients;

   typedef std::vector< ::std_msgs::ColorRGBA_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::std_msgs::ColorRGBA_<ContainerAllocator> >::other >  _diffuses_type;
  _diffuses_type diffuses;

   typedef std::vector< ::std_msgs::ColorRGBA_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::std_msgs::ColorRGBA_<ContainerAllocator> >::other >  _speculars_type;
  _speculars_type speculars;

   typedef std::vector< ::std_msgs::ColorRGBA_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::std_msgs::ColorRGBA_<ContainerAllocator> >::other >  _emissives_type;
  _emissives_type emissives;

   typedef uint8_t _block_type;
  _block_type block;





  typedef boost::shared_ptr< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SetVisualColorsRequest_

typedef ::deepracer_msgs::SetVisualColorsRequest_<std::allocator<void> > SetVisualColorsRequest;

typedef boost::shared_ptr< ::deepracer_msgs::SetVisualColorsRequest > SetVisualColorsRequestPtr;
typedef boost::shared_ptr< ::deepracer_msgs::SetVisualColorsRequest const> SetVisualColorsRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepracer_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'gazebo_msgs': ['/opt/ros/kinetic/share/gazebo_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'trajectory_msgs': ['/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "52f74642913b71ec583802100623aef1";
  }

  static const char* value(const ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x52f74642913b71ecULL;
  static const uint64_t static_value2 = 0x583802100623aef1ULL;
};

template<class ContainerAllocator>
struct DataType< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepracer_msgs/SetVisualColorsRequest";
  }

  static const char* value(const ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string[] link_names\n\
string[] visual_names\n\
std_msgs/ColorRGBA[] ambients\n\
std_msgs/ColorRGBA[] diffuses\n\
std_msgs/ColorRGBA[] speculars\n\
std_msgs/ColorRGBA[] emissives\n\
bool block\n\
\n\
================================================================================\n\
MSG: std_msgs/ColorRGBA\n\
float32 r\n\
float32 g\n\
float32 b\n\
float32 a\n\
";
  }

  static const char* value(const ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.link_names);
      stream.next(m.visual_names);
      stream.next(m.ambients);
      stream.next(m.diffuses);
      stream.next(m.speculars);
      stream.next(m.emissives);
      stream.next(m.block);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SetVisualColorsRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepracer_msgs::SetVisualColorsRequest_<ContainerAllocator>& v)
  {
    s << indent << "link_names[]" << std::endl;
    for (size_t i = 0; i < v.link_names.size(); ++i)
    {
      s << indent << "  link_names[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.link_names[i]);
    }
    s << indent << "visual_names[]" << std::endl;
    for (size_t i = 0; i < v.visual_names.size(); ++i)
    {
      s << indent << "  visual_names[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.visual_names[i]);
    }
    s << indent << "ambients[]" << std::endl;
    for (size_t i = 0; i < v.ambients.size(); ++i)
    {
      s << indent << "  ambients[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::std_msgs::ColorRGBA_<ContainerAllocator> >::stream(s, indent + "    ", v.ambients[i]);
    }
    s << indent << "diffuses[]" << std::endl;
    for (size_t i = 0; i < v.diffuses.size(); ++i)
    {
      s << indent << "  diffuses[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::std_msgs::ColorRGBA_<ContainerAllocator> >::stream(s, indent + "    ", v.diffuses[i]);
    }
    s << indent << "speculars[]" << std::endl;
    for (size_t i = 0; i < v.speculars.size(); ++i)
    {
      s << indent << "  speculars[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::std_msgs::ColorRGBA_<ContainerAllocator> >::stream(s, indent + "    ", v.speculars[i]);
    }
    s << indent << "emissives[]" << std::endl;
    for (size_t i = 0; i < v.emissives.size(); ++i)
    {
      s << indent << "  emissives[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::std_msgs::ColorRGBA_<ContainerAllocator> >::stream(s, indent + "    ", v.emissives[i]);
    }
    s << indent << "block: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.block);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPRACER_MSGS_MESSAGE_SETVISUALCOLORSREQUEST_H
