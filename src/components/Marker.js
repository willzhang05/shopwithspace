import React from 'react';
import { connect } from 'react-redux';

class Marker extends React.Component {
  componentDidMount() {
    // https://icons.duckduckgo.com/ip3/www.walmart.com.ico
  }
  render() {
    return <div className='marker'>{this.props.obj.name}</div>;
  }
}
export default connect(null, null)(Marker);
