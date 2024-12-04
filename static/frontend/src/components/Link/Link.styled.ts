import styled from "styled-components";

export const Text = styled.a`
  font-family: Actay Wide;
  font-size: 12px;
  font-weight: 700;
  line-height: 1.26;
  color: #7ed2ff;
  text-transform: none;
  text-decoration: underline;
  transition: opacity 0.3s ease-in-out;

  &:hover {
    cursor: pointer;
    opacity: 0.7;
  }
`;
