import React from 'react';
import { connect } from 'react-redux';

class StoreDetails extends React.Component {
  render() {
    let phone =
      'formatted_phone_number' in this.props.obj.details
        ? this.props.obj.details.formatted_phone_number
        : 'Unknown';
    let website =
      'website' in this.props.obj.details
        ? this.props.obj.details.website
        : 'Unknown';
    return (
      <div className='details'>
        <h2>{this.props.obj.name}</h2>

        <div className='container'>
          <h4>Business Info</h4>
          <div className='modal-contact'>
            <div className='row'>
              <h4>Address</h4>
              <p>
                {this.props.obj.details.formatted_address.substring(
                  0,
                  this.props.obj.details.formatted_address.indexOf(',')
                )}
              </p>
            </div>
            <div className='row'>
              <h4>Phone</h4>
              <p>{phone}</p>
            </div>
            <div className='row'>
              <h4>Website</h4>
              <a href={'https://' + website} target='_blank'>
                {website}
              </a>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    current: state.current,
    obj: state.stores[state.current]
  };
};

export default connect(mapStateToProps, null)(StoreDetails);
