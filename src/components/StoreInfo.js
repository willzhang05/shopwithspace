import React from 'react';
import { connect } from 'react-redux';

class StoreInfo extends React.Component {
  render() {
    return (
      <div className='store-modal-container'>
        <div className='store-modal'>
          <div className='model-content'>
            <h2>{this.props.obj.name}</h2>

            <div className='model-popular-times'></div>
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

export default connect(mapStateToProps, null)(StoreInfo);
