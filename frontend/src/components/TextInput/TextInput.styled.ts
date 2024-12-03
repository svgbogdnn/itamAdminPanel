import styled, { css } from "styled-components";

export const Input = styled.input<{ $error: boolean; $isValid: boolean }>`
  width: 100%;
  padding: 16px 18px;
  background-color: transparent;
  font-family: Monocraft;
  font-size: 12px;
  font-weight: 500;
  line-height: 1.11;
  border: 1px solid #ffffff;
  border-radius: 6px;
  color: #ffffff;

  &::placeholder {
    color: #ffffff;
    font-family: Monocraft;
    font-size: 12px;
    font-weight: 500;
    line-height: 1.11;
  }

  ${({ $error }) => {
    if ($error) {
      return css`
        color: #F93C65;
        border: 1px solid #F93C65;

        &::placeholder {
          color: #F93C65;
        }
      `;
    }

    return null;
  }}

${({ $isValid }) => {
    if ($isValid) {
      return css`
        color: #56FF9E;
        border: 1px solid #56FF9E;

        &::placeholder {
          color: #56FF9E;
        }
      `;
    }

    return null;
  }}
`;
