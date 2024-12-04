import styled from 'styled-components';

export const Label = styled.label`
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  gap: 0 8px;
`;

export const Checkbox = styled.input`
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0 0 0 0);

  &:checked + span {
    background-color: transparent;
    border: 1px solid #ffffff;

    &::after {
      transform: rotate(45deg);
      opacity: 1;
      visibility: visible;
    }
  }

  &:disabled + span {
    background-color: rgba(209, 209, 214, 0.2);
    border: 1px solid #d1d1d6;
  }
`;

export const CustomCheckbox = styled.span<{
  $isDisabled: boolean;
}>`
  flex-shrink: 0;
  display: block;
  width: 16px;
  height: 16px;
  background-color: transparent;
  border: 1px solid #ffffff;
  border-radius: 4px;
  position: relative;
  cursor: pointer;

  &::after {
    content: '';
    display: block;
    width: 4px;
    height: 8px;
    border: solid #ffffff;
    border-width: 0 2px 2px 0;
    border-radius: 2px;
    transform: rotate(0);
    opacity: 0;
    visibility: hidden;
    transition: 0.3s ease-in-out;
    transition-property: transform, opacity, visibility;
    position: absolute;
    top: 1px;
    left: 4px;
  }
`;

export const LabelContent = styled.div`
  font-family: Actay Wide;
  font-weight: 700;
  font-size: 12px;
  line-height: 1.26;
  color: #7ED2FF;
  padding: 2px 0 0;
  text-decoration: underline;
  cursor: pointer;
`;
