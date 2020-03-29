import React from 'react';
import { connect } from 'react-redux';
import PopularTimes from './PopularTimes';
import StoreDetails from './StoreDetails';
import SafetyRating from './SafetyRating';
import { viewDetailedInfo } from './StoreInfoActions';
class StoreInfo extends React.Component {
  closeModal() {
    this.props.viewDetailedInfo(null);
  }
  render() {
    let populartimes = null;
    if ('populartimes' in this.props.obj.popular) {
      populartimes = <PopularTimes />;
    }
    return (
      <div className='store-modal-container'>
        <div className='store-modal'>
          <div className='modal-content'>
            <StoreDetails />
            {populartimes}
          </div>
          <div className='modal-right'>
            <SafetyRating />
          </div>
          <div className='modal-close' onClick={this.closeModal.bind(this)}>
            <i className='far fa-times-circle'></i>
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

const mapDispatchToProps = {
  viewDetailedInfo
};

export default connect(mapStateToProps, mapDispatchToProps)(StoreInfo);
