# tcl-property

## Prerequisite
### Evironments
* [virtualenv](https://virtualenv.pypa.io/en/stable/)
    > **virtualenv** is a tool to create isolated Python environments.

    * virtualenv 를 통해 가상환경을 생성하여 작업함
    * 파이썬의 패키지 관리자인 pip 는 패키지를 global 하게 관리하므로 가상환경을 사용해야 다른 프로젝트와 라이브러리 충돌이 발생하지 않음
        * [pipenv](https://pipenv.readthedocs.io/en/latest/) 를 사용하면 내부적으로 virtualenv 를 자동으로 관리해주므로, 따로 virtualenv 를 설치할 필요가 없다고 한다. (추후에 pipenv 기반으로 환경 설정하면 좋을듯함)

    * 가상환경 만들기

        ```bash
        $ virtualenv -p python3 ./env_dir
        ```

    * 가상환경 실행

        ```bash
        $ source ./env_dir/bin/activate
        (env_dir) $
        ```

    * 가상환경 종료
        
        ```bash
        (env_dir) $ deactivate
        ```

### Packages
* [Jupyter](http://jupyter.org/)
    > The **Jupyter Notebook** is an open-source web application that allows you to create and share documents that contain live code, equations, visualizations and narrative text. Uses include: data cleaning and transformation, numerical simulation, statistical modeling, data visualization, machine learning, and much more.

    * Juptter 실행 (~~작업 디렉토리에서 실행할 것~~ default home directory 설정 가능)
        
        ```bash
        $ jupyter notebook
        ```

* [request](http://docs.python-requests.org/en/master/)
    >  **Requests** is an elegant and simple HTTP library for Python, built for human beings.


* [pandas](https://pandas.pydata.org/)
    > **pandas** is a Python package providing fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.
    * [10min. to pandas](https://pandas.pydata.org/pandas-docs/stable/10min.html)
        * pandas 의 간단한 사용법을 빠르게 익힐 수 있는 튜토리얼 제공

## 개발
### Data sources
* [공공데이터포털](ttps://www.data.go.kr/)
* [공동주택관리정보시스템](http://www.k-apt.go.kr/kaptinfo/openkaptinfo.do)