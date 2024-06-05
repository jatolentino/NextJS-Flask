// components/Modal.tsx
import React from 'react';
import { AiOutlineClose } from 'react-icons/ai';
import { TransformWrapper, TransformComponent } from 'react-zoom-pan-pinch';
// import systemdesign from './system-design.svg'

interface ModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const Modal: React.FC<ModalProps> = ({ isOpen, onClose }) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div className="bg-white rounded-lg shadow-lg overflow-hidden relative">
        <button 
          className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
          onClick={onClose}
        >
          <AiOutlineClose size={24} />
        </button>
        <div className="p-4">
          <h2 className="text-xl font-semibold mb-4 text-center align-center justify-center">System Design</h2>
          <div className="border border-gray-300 rounded-lg overflow-hidden cursor-grab">
            <TransformWrapper>
              <TransformComponent>
                <img
                  src="./system-design.svg"
                  alt="system-design"
                  className="h-[75vh]"
                />
                
              </TransformComponent>
            </TransformWrapper>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Modal;
